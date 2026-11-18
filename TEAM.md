# Team

## Thông tin nhóm

- Tên nhóm: Nhom5Nguoi
- Lớp: L3A
- Repo của bàn: `K5-L3A-DAY10-Nhom5Nguoi-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): **S8** — trưởng ca CSKH không tin trợ lý, kiểm tay mọi quyết định.

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |     Đồng Ngọc Phúc      |   2A202603399   |  Kỹ sư cổng   | X|
|   2 |     Vũ Văn Hảo      |   2A202603419   |  Kỹ sư cổng   |             |
|   3 |     Nguyễn Trần Anh Khôi      |  2A202603422    |  Kỹ sư cổng   |             |
|   4 |     Nguyễn Việt Hưng     |   2A202603411   |  Sản phẩm và kinh doanh   |             |
|   5 |     Nguyễn Huy Hoàng     |   2A202603366   |  Vận hành và pháp lý   |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Phân công và thứ tự phối hợp

Đây là phân công cần thực hiện, không phải xác nhận mọi người đã hoàn thành. Mỗi người tự cập nhật đóng góp, bằng chứng và exit ticket của mình trước khi nộp.

### Việc làm ngay · Khối 2A (chưa sửa guard hoặc config vận hành)

| Người phụ trách | Câu / mục phiếu | Công việc cụ thể | Sản phẩm bàn giao |
|---|---|---|---|
| Đồng Ngọc Phúc | 2.1 · B0 dòng 1, B1; điều phối 2.5 · B6 | Kiểm tra phân tích baseline, đối chiếu tiêu chí đã ký; tổng hợp kết quả B2–B5 và chủ trì pre-mortem bốn lăng kính. | B0–B1 có mã chạy và số liệu; B6 sau thảo luận chung. Baseline đã chạy: `R-base-before-20261118-154608-bde05c`, hoàn sai 20.000đ và 1 lỗi hãng oan tại `T-002@55`. |
| Vũ Văn Hảo | 2.2 · B2 | Chạy `python -m lab10.trace --suite base --ticket T-002 --seed 55`; xác định bước sai đầu tiên; điền đủ ba phần ghi lỗi, tìm nguồn và hướng xử lý. | B2 có dòng trace, loại lỗi, người chịu hại và hướng xử lý; không chỉ ghi kết quả cuối. |
| Nguyễn Trần Anh Khôi | Hỗ trợ 2.2 · B2; chuẩn bị 2.7–2.8 | Đối chiếu trace của Hảo với tracking/chính sách, kiểm tra cả thao tác hoàn tiền và ghi lỗi hãng; đề xuất một tính chất và hai ticket mới để kiểm sau khi có guard. | Góp ý cho Hảo tích hợp vào B2; gửi dự thảo behavioral test cho cả nhóm, chưa ghi rằng đã chạy test. |
| Nguyễn Việt Hưng | 2.3 · B3 | Điền bản đồ dữ liệu: trường then chốt, nguồn sự thật/bản sao, điểm có thể lệch; viết một ví dụ drift có thời điểm, trường thay đổi, metric bị ảnh hưởng và tín hiệu phát hiện. | B3 hoàn chỉnh, dẫn dữ liệu trong `data/world.json`; phân biệt đầu vào đổi và quan hệ vào–ra đổi. |
| Nguyễn Huy Hoàng | 2.4 · B4–B5 | HAZOP trên một tool ghi: ít nhất 3 dòng, thêm ít nhất 2 dòng ngoài kỹ thuật; điền checklist 9 nhóm việc với trạng thái, bằng chứng và PIC có tên. | B4–B5 hoàn chỉnh; các việc chưa làm ghi đúng trạng thái, không ghi hoàn tất nếu chưa có bằng chứng. |

Sau khi có B2–B5, cả nhóm cùng làm B6: kỹ thuật, kinh doanh, con người/vận hành, pháp lý; chọn 2–3 nguyên nhân để biến thành cổng vòng 1.

### Khối 2B · Cổng phòng ngừa và quyết định v1

| Người phụ trách | Câu / mục phiếu | Công việc và file |
|---|---|---|
| Đồng Ngọc Phúc | 2.6 · B7.1; B0, B8 | Tích hợp và sở hữu bản sửa cuối của `lab10/guards.py`; nhận đề xuất từ Hảo/Khôi, viết 2–3 cổng theo B6/HAZOP; chạy eval/test. Sau khi cả nhóm rà soát, chạy checkpoint đúng một lần, eval prepared, gate; ghi B0 và bằng chứng B8, commit/push bản chốt. |
| Vũ Văn Hảo | Hỗ trợ 2.6 · B7.1 | Đề xuất kiểm tra quyền lợi hoàn tiền từ tracking/chính sách và căn cứ ghi lỗi hãng; gửi code hoặc diff cho Phúc tích hợp; xác minh `T-002@55` sau sửa và ghi trace trước/sau vào B7.1. |
| Nguyễn Trần Anh Khôi | 2.7–2.8 · B7.2–B7.3 | Viết hai bước tránh rò rỉ dữ liệu đánh giá; hoàn thiện tính chất và hai ticket mới, chạy `trace --adhoc` sau khi guard được tích hợp; chạy public tests, báo ca mới hỏng và lưu bằng chứng, giữ ticket cho demo. |
| Nguyễn Việt Hưng | 2.9 · B7.4; B8 | Sở hữu `business` trong `config/operating_gates.json`: trần hoàn ngày, ngân sách LLM, phạm vi pilot và ROI; giải thích từng lựa chọn từ `ops_limits`/`ops_facts`. Soạn lý do quyết định v1 theo tiêu chí đã ký để cả nhóm chốt. |
| Nguyễn Huy Hoàng | 2.10 · B7.5–B7.6 | Sở hữu `operations` và `legal` trong config: PIC, approver, nhân sự/công suất, SLA, điều kiện dừng, kênh báo tin, PII và căn cứ lỗi hãng; viết runbook 1–3, thời hạn dừng và phương án giờ cao điểm khớp config. |

Phúc là người tích hợp config chung: Hưng và Hoàng chỉ sửa mục được giao, đồng bộ lần lượt để tránh xung đột. Chỉ chốt vòng 1 khi cả ba mảng code, business và operations/legal đã được rà soát. Quyết định v1 do cả nhóm thống nhất, không phải quyết định riêng của người ghi phiếu.

### Vòng 2 · Phân công cụ thể cho thẻ S8

**Đã nhận:** commit `e75155b`, sau commit chốt v1 `162a430`. Phúc đã dùng AI đọc đúng thẻ S8, ghi số thẻ và chạy grade trước mọi sửa đổi code/config vòng 2. Grade `R-S8-grade-20261118-164813-3cce15`; C0–C1 đã có bằng chứng. Prepared xử lý đúng 260/260, 0 hoàn sai/lỗi hãng/PII, 0 ùn; tổng grade FAIL vì integrity và chưa có monitor mới. Không sửa snapshot hay tiêu chí đã ký.

| Người | Việc làm ngay | Bàn giao / điều kiện hoàn thành |
|---|---|---|
| **Phúc** | Điều phối, sở hữu C0–C1 và xử lý lỗi integrity với Coach. Tổng hợp C6/C9 cùng nhóm; sau khi nhận phần việc, chạy grade/regression, tích hợp C7/C12 và chuẩn bị demo. | Báo Coach: 23 file khớp hash khi chuẩn hóa CRLF→LF trong bộ nhớ, 28 file thiếu thuộc S1–S7 do chỉ được lấy S8. Không sửa MANIFEST/bộ chấm hoặc lấy thẻ khác. Ghi lại hướng dẫn thật của Coach, không tự xác nhận integrity đạt. |
| **Hảo** | **C2**, góp C4/C6/C7: trace base `S8-01`, `S8-02`, `S8-03`, `S8-06` (seed 11), chọn ít nhất hai kiểu sai khác nhau; đối chứng `S8-05` hợp lệ và so prepared. | Dán approval_used và đối chiếu approvals: sai ticket/đơn/khách, hết hạn/thu hồi, vượt max_vnd; phân biệt lỗi chìm với hệ quả mất niềm tin. Chứng minh ca hợp lệ vẫn được phục vụ; không sửa guard chỉ để tạo khác biệt khi prepared đã đạt. |
| **Khôi** | **C8**, sở hữu `lab10/monitors.py`; hỗ trợ C7 và regression. Thiết kế ít nhất một monitor mới bắt nguyên nhân S8, chỉ dùng monitor_view (không label/pass/wrongful_refund). | Đề xuất đếm sự kiện cổng từ chối/chuyển người vì approval và/hoặc rủi ro review; đăng ký MONITORS, viết đủ thước đo→dữ liệu→cách tính, kiểm base so S8 có tín hiệu khác nhau. Nếu cần thêm event guard phải phối hợp Phúc để không sửa chồng file; không dùng ID S8 làm điều kiện. |
| **Hưng** | **C5 câu 3.2**, hỗ trợ C7/C12: specification phê duyệt và điều kiện kinh tế; đọc staff_behavior và report ba mốc, phân tích DN/chi phí, thời gian chờ và ROI. | Nêu số trước/sau đúng đơn vị; DN prepared có chi phí cao nhất 3.200đ/ticket; mọi kho đạt. Đề xuất v2 có điều kiện dựa trên số và integrity, không chọn Tiếp tục khi integrity chưa giải quyết; không tăng người hay thu hẹp vô cớ. |
| **Hoàng** | **C3.4 Hiệu chỉnh lòng tin** cho nhân viên duyệt và trưởng ca, thêm một dòng hoàn trên hạn mức ở **C3.1 Bước 2**; **C4 >=3 dòng**, **C5 câu 3.3**, **C10–C11**. | Giải thích hai mốc tin quá mức/không tin và bằng chứng cần để tin vừa đủ; kiểm approver_id/decision_note/sampling khớp staff_behavior; risk register, checklist 9 nhóm có PIC, runbook 4–5 (điều kiện kiểm mẫu/bật lại, quyền duyệt, kiểm toán). Không ghi nhận phê duyệt của NV-HANH chưa có thật. |

**Cách phối hợp:** mỗi người sửa đúng mục phiếu được giao; Khôi sửa monitors, Hưng/Hoàng chỉ đề xuất config nếu có nguyên nhân cần đổi. Phúc tích hợp guards/config và chạy lần cuối. C6/C9 do cả nhóm cung cấp nhánh, Phúc tổng hợp. Giữ nguyên Phiếu B/v1. Chỉ hoàn thành C12/submission sau khi có monitor và report cuối; hiện chưa có quyết định v2.

**Lệnh trace cho Hảo (thay ID bằng đúng ticket S8 cần dò):** `python -m lab10.trace --suite S8 --stage base --ticket S8-01 --seed 11`; so với cùng lệnh `--stage prepared`. Grade chung: `python -m lab10.grade --incident S8`.

### Gom bài và phối hợp Git

- Hoàng điền `submission/submission.json`, chạy hoặc phối hợp Phúc chạy `python -m lab10.check_submission --collect`; xử lý mục thiếu cùng người sở hữu phần đó.
- Phúc kiểm report khớp code/config cuối, tổng hợp commit/push; sau demo phải trả cấu hình về bản v2 và chạy lại grade/collect.
- Mỗi người sửa đúng mục phiếu được giao. Vì dùng chung Phiếu B/C, cập nhật từ `main` trước khi làm và rà diff khi tích hợp; không ghi đè phần của người khác.
- Không commit file sinh tự tạo bằng tay, không dùng mã ticket/câu chữ riêng làm quy tắc guard; giữ nguyên file khóa và bản chốt.
- Mỗi thành viên tự hoàn thiện mục cá nhân bên dưới, ghi rõ có dùng AI cho phần nào, và tự nộp link repo trên LMS theo hạn Coach quy định.

## Cá nhân

## DongNgocPhuc-2A202603399

### Phần việc phụ trách

Trưởng nhóm, kỹ sư cổng và tích hợp: B0–B1, điều phối B6, B7.1, checkpoint/prepared và B8; vòng 2 C0–C1, C7, tổng hợp C12, chạy báo cáo và demo. Hỗ trợ nhóm chuẩn bị Phiếu A từ bộ tài liệu Lab 9 đã chọn.

### Đóng góp cụ thể

Đã cung cấp kết quả baseline `R-base-before-20261118-154608-bde05c`. Đã dùng ChatGPT hỗ trợ đọc lab, soạn Phiếu A, phân tích B0–B1 và phân công công việc. Đã dùng AI hoàn thiện B6 từ phần việc nhóm bàn giao; tích hợp G1–G3, kiểm tra 13 public tests, eval after/prepared, hai behavioral ticket × 5 seed và ca có số điện thoại; chốt snapshot vòng 1, cập nhật B0/B5/B7 và quyết định v1 Cải tiến thêm. Không nhận thay phần nghiên cứu ban đầu của Hảo, Khôi, Hưng, Hoàng; không ghi nhận buổi họp hoặc chữ ký chưa được xác minh.

### Bằng chứng

Baseline: `runs/R-base-before-20261118-154608-bde05c/report.json`; B0 dòng 1 và B1. Commit ký `19f0edf`; after `R-base-after-20261118-163822-3cce15`; prepared `R-base-prepared-20261118-163931-3cce15`; snapshot `518a9ba2`; kết quả 110/110, tiền sai/lỗi hãng/PII=0, chi phí 4.456đ/ticket, ROI 1,24. B6/B7/B8 ghi đầy đủ bằng chứng; mã commit tích hợp xác định sau khi commit thực tế.

### Exit ticket

Phúc tự điền trước khi nộp: một điều học được và một điều còn chưa chắc.

## VuVanHao-2A202603419

### Phần việc phụ trách

Kỹ sư cổng: B2; hỗ trợ B7.1 (kiểm quyền lợi hoàn, căn cứ ghi lỗi hãng); vòng 2 C2, phân tích nguyên nhân và đề xuất sửa kỹ thuật cho C7; cùng nhóm B6 và fault tree.

### Đóng góp cụ thể

- **Vòng 1 · Khối 2A (B2):** Chạy trace trên `T-002@55` (`stage base`), xác định bước sai đầu tiên tại `03 model_override {"field": "delay_days", "db": 2, "ticket": 5}` (model lấy 5 ngày khách tự khai đè lên `db_delay_days: 2` của tracking DB), dẫn tới hai lỗi chìm nối tiếp ở `06 issue_refund` (hoàn sai `20.000đ` gây lệch sổ cho LogiX / chị Oanh `NV-OANH`) và `07 file_carrier_fault` / `08 notify_carrier` (ghi 1 lỗi oan cho hãng `VNX` và tài xế `TX-VNX-03`). Đã hoàn thành đủ 3 phần của bảng soát lỗi ở Phiếu B mục B2.
- **Vòng 1 · Khối 2B (hỗ trợ B7.1 & `lab10/guards.py`):** Cài đặt 2 nhánh cổng trong `write_gate(ctx, action)` dùng nguồn sự thật từ `lab10/helpers.py` (`effective_policy`, `ticket_parcel`, `db_delay_days`, `entitlement_vnd`, `carrier_at_fault`) và `ctx.tools`: (1) kiểm tra trùng hoàn và đối chiếu quyền lợi hoàn tiền theo tracking DB/chính sách hiệu lực trước `issue_refund` (`deny` nếu quyền lợi `<= 0` hoặc đã hoàn, `modify` nếu lệch số tiền/`payer`, `escalate` nếu vượt `auto_limit_vnd` thiếu `approval_id`); (2) kiểm tra căn cứ ghi lỗi hãng trước `file_carrier_fault` (`deny` nếu `carrier_at_fault` là `False`, `modify` để đồng bộ `parcel_id`/`carrier_id`/`driver_id`/`delay_days` từ DB). Đã xác minh lại `T-002@55` ở `--stage after` (chuyển từ `HỎNG` sang `ĐẠT {}`, `SỔ CÁI: []`, `LỖI HÃNG: []`) và chạy `unittest discover -s tests` đạt `13/13 OK` (không làm hỏng ca nền nào). Đã ghi đối chiếu trace trước/sau vào Phiếu B mục B7.1 để Phúc rà soát/tích hợp cùng nhóm và Khôi kiểm tra thêm.
- **Vòng 2 (`C2`, `C7`) & thảo luận chung (`B6`, fault tree):** Chờ nhóm làm tiếp B6 và tới mốc nhận thẻ phút 125 sẽ tự bổ sung sau khi hoàn thành.
- **Sử dụng AI:** Có dùng Antigravity hỗ trợ đọc cấu trúc codebase (`guards.py`, `helpers.py`, `agent.py`, `world.json`), đối chiếu trace `T-002@55`, viết nháp hai nhánh `write_gate` và biên soạn bảng B2/B7.1; đã trực tiếp chạy kiểm tra lại bằng `lab10.trace` và `unittest` trên máy.

### Bằng chứng

- **Trace trước sửa (`T-002@55 · stage base`):** `03 model_override {"field": "delay_days", "db": 2, "ticket": 5}` → `06 tool issue_refund` (`20.000đ`) & `07 tool file_carrier_fault` (`VNX`, `delay_days: 5`) → `KẾT QUẢ : HỎNG {'status': False, 'refund_amount': False, 'carrier_fault': False}`.
- **Trace sau sửa (`T-002@55 · stage after`):** `06 guard {"kind": "guard_refund_no_entitlement", "order_id": "O-1002", "db_delay_days": 2, "asked_vnd": 20000, "cause": "CARRIER"}` → `07 gate {"tool": "issue_refund", "action": "deny", ...}` → `08 tool send_reply` (`amount_vnd: 0`) → `SỔ CÁI : []`, `LỖI HÃNG : []`, `GỬI HÃNG : []`, `KẾT QUẢ : ĐẠT {}`.
- **Unit tests:** `python -m unittest discover -s tests -v` → `Ran 13 tests in 0.812s · OK` (gồm `test_team_guards_do_not_break_base`).
- **File & mục đã điền:** `lab10/guards.py` (`write_gate`), `templates/form-b-evaluation-gates.md` (mục `B2` và phần hỗ trợ `B7.1`). Mã commit đóng góp và phần vòng 2 (`C2`, `C7`) sẽ bổ sung sau khi commit và sau phút 125.

### Exit ticket

- **Một điều học được:** Cổng kiểm tra trước khi ghi (`write_gate`) đối chiếu trực tiếp với nguồn sự thật (tracking DB + chính sách hiệu lực) quan trọng hơn việc sửa prompt, vì cùng một ticket (`T-002`), model có thể đúng ở `seed 11` nhưng tự tin sai ở `seed 55` và gây lỗi chìm cho cả kế toán lẫn hãng vận chuyển.
- **Một điều còn chưa chắc:** Hai nhánh `write_gate` vòng 1 đã chặn hoàn sai và lỗi hãng oan dựa trên DB, nhưng chưa biết ở vòng 2 sự cố có đến từ nhánh khác như dữ liệu đầu vào/phiên bản chính sách/người nhận hay hàng chờ vận hành không — cần đối chiếu thêm sau khi làm B6 với nhóm và nhận thẻ sự cố ở phút 125.

## NguyenTranAnhKhoi-2A202603422

### Phần việc phụ trách

Kỹ sư cổng: hỗ trợ B2; B7.2–B7.3 (tránh rò rỉ dữ liệu đánh giá, behavioral test), public tests/regression; vòng 2 C8 và `lab10/monitors.py`; cùng nhóm B6 và fault tree.

### Đóng góp cụ thể

Khôi tự ghi sau khi làm: tính chất và hai ticket mới đã chạy, kết quả test, monitor đã thêm và phần có sử dụng AI nếu có.

### Bằng chứng

Khôi tự bổ sung mã commit, câu lệnh/kết quả adhoc, mã report có monitor và kết quả regression.

### Exit ticket

Khôi tự điền trước khi nộp: một điều học được và một điều còn chưa chắc.

## NguyenVietHung-2A202603411

### Phần việc phụ trách

Sản phẩm và kinh doanh: rà soát, giải thích mục tiêu/ngưỡng Phiếu A đã được nhóm thống nhất; B3, B7.4 và mục `business` trong config; soạn căn cứ B8/C12; vòng 2 specification ở C5, phân tích kinh tế và thay đổi phạm vi ở C7.

### Đóng góp cụ thể

Vòng 1 (đã làm):
- **Phiếu A · rà soát sau khi ký**: kiểm lại các phép tính ở A4 (106/110 = 0,9636 ≥ 0,96; 20/22 = 0,909 ≥ 0,90; ROI 2.000/8.000 = 0,25 tương đương trần 8.000đ/ticket; escalation 0,30 × 10.000đ ≈ 3.000đ/ticket) và câu 1.5 so với đề; điền A5 (ký `2026-11-18T15:44:18`, commit `19f0edf` đã có trên `origin/main`, `lab10.criteria verify` → ok) và dòng "Bàn". Không sửa nội dung A1–A4 đã viết trước khi ký.
- **B3 · Bản đồ dữ liệu**: người dùng trực tiếp và bên thứ ba, 4 lệnh ghi, các bảng trợ lý đọc; tách **nguồn sự thật** (`promised_date`, `delivered_date`, `delay_cause`, phí/giá trị đơn, ngày hiệu lực chính sách, `approvals`, sổ cái) khỏi **bản sao** (`refund_status` làm mới ban đêm, cờ `index_active`, số ngày khách tự khai); các định dạng dễ sai (`delivered_date: null`, đơn nhiều kiện `O-1013`, đơn không tồn tại, đơn quà).
- **Ví dụ drift**: REFUND-v3 → v4 ngày 2026-12-01 (trợ lý chọn chính sách theo `index_active` chứ không theo ngày). Đây là **quan hệ vào–ra đổi**: cùng đơn trễ 2 ngày đổi từ từ chối sang hoàn 20.000đ; FORCE_MAJEURE không còn ghi lỗi hãng; `auto_limit` 200.000 → 100.000đ. Chỉ ra các ngưỡng đã ký bị ảnh hưởng và đề xuất chỉ số `policy_mismatch` (không cần nhãn).
- **B7.4 + `config/operating_gates.json` mục `business`**: `daily_refund_cap_vnd` 1.500.000 (hoàn tự động ≈ 453.000đ/ngày × 3 cao điểm, chừa 500.000đ dưới ngân sách Finance 2.000.000đ); `cost_budget_per_ticket_vnd` 1.500 (= trần Ops/Finance); `pilot_scope` all (mọi kho rẻ hơn làm tay, lỗi không gắn kho); `roi_min` 0,25 (= tiêu chí đã ký, tương đương ≤ 8.000đ/ticket). Đã thử trên bộ nền: không ca mới hỏng, không vượt trần, 13 test OK.
- **B8 · Dự thảo căn cứ quyết định v1**: điền các ô đã có bằng chứng, đề xuất **Cải tiến thêm** theo `decision_rule` đã ký, kèm cây quyết định A–D để cả nhóm chốt khi có mốc prepared.
- Có dùng AI (Claude Code) để đọc dữ liệu/code lab, tính các con số, chạy eval/test và soạn nháp B3, B7.4, B8; Hưng rà lại số liệu với `data/world.json` và report.

Chưa làm: vòng 2 (C5, C7, C12) chờ thẻ sự cố; chốt v1 chờ prepared.

### Bằng chứng

- Config: `config/operating_gates.json` → `business` (4 khoá); nguồn số: `data/world.json` → `ops_limits` (`daily_auto_refund_budget_vnd`, `max_llm_cost_per_ticket_vnd`), `ops_facts` (`manual_cost_per_ticket_vnd`, `review_cost_per_ticket_vnd`, `review_capacity_per_reviewer_per_hour`, `llm_cost`), `policies[]` (REFUND-v3/v4), `orders[].parcels`, `approvals`; `data/tickets.jsonl` (tổng hoàn đúng 683.000đ/ngày).
- Lần chạy thử cổng business: `R-base-after-20261118-161730-6f4f66` (nhật ký trên máy của Hưng). Report so sánh: `R-base-before-20261118-154608-bde05c`.
- Mục phiếu: Phiếu B B3, B7.4, B8 (dự thảo). Mã commit: bổ sung sau khi đẩy.

### Exit ticket

Hưng tự điền trước khi nộp: một điều học được và một điều còn chưa chắc.

## NguyenHuyHoang-2A202603366

### Phần việc phụ trách

Vận hành và pháp lý: rà soát mục tiêu Oanh/Hạnh và telemetry Phiếu A; B4–B5, B7.5–B7.6 và mục `operations`/`legal` trong config; vòng 2 phần riêng của thẻ, HAZOP, giả định môi trường, risk register/checklist/runbook ở C3–C5/C9–C11; gom bài nộp.

### Đóng góp cụ thể

Vòng 1 (đã làm):
- **B4 · HAZOP vòng 1** trên `issue_refund`: 5 dòng kỹ thuật (WRONG thấy trên trace `T-002@55`; INVALID chính sách/phê duyệt, INCOMPLETE đơn chưa giao/nhiều kiện, PERTURBED `directive` hoàn toàn bộ đơn, INCAPABLE LLM `fail_open` — các nhánh chưa thấy trên trace) và 4 dòng ngoài kỹ thuật (dữ liệu gửi bên thứ ba, người duyệt, ngân sách, người đứng tên duyệt).
- **B5 · Checklist 9 nhóm việc lần 1**: mỗi dòng có PIC tên người; cả 9 dòng ghi **Chưa** vì chưa có guard, `business`, B2/B3, monitor mới và mốc prepared.
- **Config `operations` + `legal`**: PIC `NV-TUNG`, approver `NV-HANH`, 1 người trực, 6 ca/giờ, chờ tối đa 60 phút, 6 điều kiện dừng, kênh báo tin, `decision_note: true`, kiểm mẫu 10%; chặn 7 trường PII gửi hãng; ghi lỗi hãng phải có nguyên nhân trong tracking.
- **B7.5 · Runbook 1–3** (người chịu trách nhiệm, 7 tín hiệu vàng/đỏ, cách dừng, thời hạn dừng 15 phút, điều kiện bật lại) và **B7.6 · Giờ cao điểm**, khớp config.
- Có dùng AI (Claude Code) để đọc code/dữ liệu lab, chạy eval/trace và soạn nháp B4, B5, B7.5–B7.6, config; Hoàng rà lại các con số với report trước khi nộp.

Chưa làm: vòng 2 (C3–C5, C9–C11, runbook 4–5) chờ thẻ sự cố; gom bài `submission.json` và `check_submission --collect`.

### Bằng chứng

- Lần chạy: `R-base-after-20261118-160422-0cb2ae` (config operations/legal), `R-base-after-20261118-160436-2a7275` (thử 2 người trực) — Phiếu B mục B0 dòng 4–5.
- Phiếu B mục B4, B5, B7.5, B7.6; `config/operating_gates.json` mục `operations`, `legal`.
- Mã commit và kết quả `check_submission` thực tế: bổ sung khi có.

### Exit ticket

- **Một điều học được:** cổng config đúng chưa chắc chặn được lỗi. Trên `T-002@55`, bật `carrier_fault_requires_recorded_cause` không ngăn được lỗi ghi oan cho VNX. Tracking vẫn ghi nguyên nhân CARRIER, cái sai là trợ lý lấy số ngày khách tự khai (5 ngày) đè lên DB (2 ngày). Vì vậy phải biết lỗi nằm ở tầng nào (dữ liệu đầu vào hay quy tắc ghi) rồi mới chọn cổng; mỗi cổng phải kiểm lại bằng một lần chạy có mã (`R-base-after-20261118-160422-0cb2ae`).
- **Một điều còn chưa chắc:** 1 người trực, 6 ca/giờ có chịu được giờ cao điểm thật không. Bộ nền chỉ có khoảng 2,75 ticket/giờ, rải đều, nên chờ lâu nhất là 0 phút. Còn khi lượng ticket gấp ba hoặc LLM lỗi 429 làm tỉ lệ chuyển người tăng vọt, ngưỡng gọi thêm người (hàng chờ ≥ 4 ca, chờ ≥ 30 phút) là mình suy ra chứ chưa đo, và người trực thứ hai vẫn chưa có tên trong `staff`.
