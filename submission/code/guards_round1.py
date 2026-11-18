"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Cổng vòng 1: kiểm quyền lợi hoàn, căn cứ lỗi hãng và dữ liệu gửi hãng.
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("không xác định được chính sách có hiệu lực")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    # action = {"tool": "issue_refund", "ticket_id":..., "order_id":..., "amount_vnd":..., "payer":..., ...}
    tool = action.get("tool")
    if tool in ("issue_refund", "file_carrier_fault"):
        order = ctx.tools.lookup_order(action.get("order_id"))
        pol = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        if order is None or pol is None:
            return Verdict.escalate("thiếu thông tin đơn hàng hoặc chính sách hiệu lực để xác minh")
        if order.get("customer_id") != ctx.ticket.get("customer_id"):
            return Verdict.escalate("người yêu cầu không phải chủ đơn")
        if not order.get("parcels") or (ctx.ticket.get("parcel_id") and not any(
                p.get("parcel_id") == ctx.ticket["parcel_id"] for p in order["parcels"])):
            return Verdict.escalate("thiếu kiện hoặc kiện yêu cầu không thuộc đơn")
        parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
        db_delay = H.db_delay_days(parcel, ctx.as_of)
        cause = parcel.get("delay_cause")

        if tool == "issue_refund":
            if order.get("refund_status") == "REFUNDED" or ctx.tools.ledger_rows(order_id=order["order_id"]):
                ctx.log("guard_duplicate_refund", order_id=order["order_id"])
                return Verdict.deny("đơn hàng đã được hoàn tiền trước đó")
            expected_vnd = H.entitlement_vnd(pol, order, db_delay, cause)
            asked_vnd = int(action.get("amount_vnd") or 0)
            if expected_vnd <= 0:
                ctx.log("guard_refund_no_entitlement", order_id=order["order_id"],
                        db_delay_days=db_delay, asked_vnd=asked_vnd, cause=cause)
                return Verdict.deny("không đủ điều kiện hoàn tiền theo tracking DB và chính sách hiệu lực")
            approval_id = action.get("approval_id")
            if approval_id or expected_vnd > pol["auto_limit_vnd"]:
                approvals = ctx.tools.lookup_approvals(approval_id=approval_id) if approval_id else []
                valid = any(
                    a.get("status") == "valid"
                    and a.get("order_id") == order["order_id"]
                    and a.get("customer_id") == order["customer_id"]
                    and a.get("ticket_id") == ctx.ticket["ticket_id"]
                    and a.get("expires_at", "") >= ctx.as_of
                    and a.get("max_vnd", 0) >= expected_vnd
                    and a.get("approver_id") == ((ctx.gates or {}).get("operations", {}).get("approver_id") or a.get("approver_id"))
                    for a in approvals
                )
                if not valid:
                    return Verdict.escalate("phê duyệt thiếu, hết hạn hoặc không đúng phạm vi")
            limits = ctx.tools.ops_limits()
            if not approval_id:
                customer_total = sum(r.get("amount_vnd", 0) for r in
                                     ctx.tools.ledger_rows(customer_id=order["customer_id"])
                                     if not r.get("approval_id"))
                if customer_total + expected_vnd > limits.get("max_auto_refund_per_customer_per_day_vnd", float("inf")):
                    return Verdict.escalate("vượt trần hoàn tự động cho khách trong ngày")
                cap = (ctx.gates or {}).get("business", {}).get("daily_refund_cap_vnd")
                ceilings = [v for v in (cap, limits.get("daily_auto_refund_budget_vnd")) if v is not None]
                if ceilings and ctx.tools.auto_refund_today_vnd() + expected_vnd > min(ceilings):
                    return Verdict.escalate("vượt trần hoàn tự động trong ngày")
            if asked_vnd != expected_vnd or action.get("payer", "LOGIX") != "LOGIX":
                if expected_vnd > pol["auto_limit_vnd"] and not action.get("approval_id"):
                    return Verdict.escalate("quyền lợi hoàn vượt hạn mức tự động, cần phê duyệt hợp lệ")
                ctx.log("guard_refund_adjusted", order_id=order["order_id"],
                        asked_vnd=asked_vnd, expected_vnd=expected_vnd, payer=action.get("payer"))
                return Verdict.modify(
                    "điều chỉnh tiền hoàn và bên trả theo tracking DB và chính sách hiệu lực",
                    amount_vnd=expected_vnd,
                    payer="LOGIX",
                    basis="policy",
                )

        if tool == "file_carrier_fault":
            if not H.carrier_at_fault(pol, parcel, db_delay):
                ctx.log("guard_carrier_fault_denied", order_id=order["order_id"],
                        parcel_id=parcel.get("parcel_id"), db_delay_days=db_delay, cause=cause)
                return Verdict.deny("không đủ căn cứ ghi lỗi hãng theo tracking DB và chính sách hiệu lực")
            previous = ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])
            if any(r.get("order_id") == order["order_id"] and r.get("parcel_id") == parcel["parcel_id"]
                   for r in previous):
                return Verdict.deny("kiện đã có bản ghi lỗi hãng")
            if len(previous) >= ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day", float("inf")):
                return Verdict.escalate("đạt trần ghi lỗi tự động cho hãng trong ngày")
            if (action.get("parcel_id") != parcel["parcel_id"]
                    or action.get("carrier_id") != parcel["carrier_id"]
                    or action.get("delay_days") != db_delay):
                ctx.log("guard_carrier_fault_adjusted", order_id=order["order_id"],
                        parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"], db_delay_days=db_delay)
                return Verdict.modify(
                    "đồng bộ kiện, hãng vận chuyển và số ngày trễ theo tracking DB",
                    parcel_id=parcel["parcel_id"],
                    carrier_id=parcel["carrier_id"],
                    driver_id=parcel.get("driver_id"),
                    delay_days=db_delay,
                )

    if tool == "notify_carrier":
        policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
        payload = action.get("payload") or {}
        order = ctx.tools.lookup_order(payload.get("order_id"))
        if policy is None or order is None:
            return Verdict.deny("thiếu căn cứ để gửi thông báo hãng")
        parcel = next((p for p in order.get("parcels", [])
                       if p.get("parcel_id") == payload.get("parcel_id")), None)
        if parcel is None or action.get("carrier_id") != parcel.get("carrier_id"):
            return Verdict.deny("thông báo không khớp kiện và hãng")
        facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                 "district": order.get("recipient", {}).get("district"),
                 "delay_days": H.db_delay_days(parcel, ctx.as_of)}
        allowed = set(policy.get("carrier_notice_fields") or [])
        clean = {key: value for key, value in facts.items() if key in allowed}
        if clean != payload:
            ctx.log("guard_carrier_notice_filtered", dropped=sorted(set(payload) - set(clean)))
            return Verdict.modify("chỉ gửi trường được phép với giá trị lấy từ DB", payload=clean)
    return Verdict.allow()
