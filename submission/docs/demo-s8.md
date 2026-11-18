# Demo S8 · Kịch bản 5 phút

Đây là kịch bản chuẩn bị, không phải xác nhận đã demo hoặc đã trả lời Coach.

## 0:00–1:00 · Vấn đề và ba mốc

Thẻ S8: chị Hạnh bị đứng tên các khoản dùng mã duyệt sai phạm vi, hết hạn hoặc thu hồi; nhân viên mất niềm tin nên kiểm tay mọi quyết định. Chỉ sửa số tiền chưa đủ: phải trả quyền kiểm soát và cung cấp chứng cứ để nhân viên kiểm mẫu có cơ sở.

| Chỉ số trên S8 | base | prepared | after |
|---|---:|---:|---:|
| Tỷ lệ lượt đúng | 86,54% | 100% | 100% |
| Tiền hoàn sai, tổng qua 5 seed | 6.845.000đ | 0đ | 0đ |
| Lỗi hãng oan | 35 | 0 | 0 |
| Nhân viên kiểm lại quyết định tự động | 100% | 10% | 10% |
| Số ca ùn | 36 | 0 | 0 |
| Chờ lâu nhất | 216 phút | 5 phút | 5 phút |
| Chi phí/ticket | 11.225đ | 2.952đ | 2.952đ |
| ROI | -2,45 | 2,39 | 2,39 |

Nguồn: `runs/grade-report.json`, grade `R-S8-grade-20261118-174256-726304`. Một người trực, 6 ca/giờ, độ phủ 100%; không dùng tăng người hoặc cắt hết phạm vi để làm xanh.

## 1:00–2:15 · Một ca sai và một ca đúng

Chạy tại gốc repo, từng lệnh riêng trong PowerShell:

```powershell
python -m lab10.trace --suite S8 --stage base --ticket S8-01 --seed 11
python -m lab10.trace --suite S8 --stage prepared --ticket S8-01 --seed 11
python -m lab10.trace --suite S8 --stage after --ticket S8-05 --seed 11
```

S8-01 base dùng A-2801 đã used và thuộc ticket cũ, ghi 230.000đ. Prepared giữ khoản trước ghi, chuyển người; không còn sổ cái/lỗi hãng. S8-05 có phê duyệt hợp lệ vẫn được hoàn 230.000đ. Không kiểm mã ticket trong guard; ID chỉ để chọn ca minh họa.

## 2:15–3:15 · Phòng ngừa và phần mới vòng 2

- Cổng vòng 1 kiểm quyền lợi, hiệu lực/phạm vi phê duyệt và ledger trước ghi; đúng hãng/kiện; tối thiểu hóa thông báo. Config có NV-HANH, ghi chú và kiểm mẫu 10%.
- Prepared đã đỡ toàn bộ ca visible S8; không nhận các cổng đó là phần sửa mới sau nhận thẻ.
- Phần mới vòng 2 là `approval_review_rate` và `human_recheck_rate`: nền 0 / 0,045455; S8 0,096154 / 0,076923. Near miss bị chặn không có nghĩa đã chi sai. Hai metric chỉ phát hiện, không tự ngăn tác hại hoặc tự gửi cảnh báo.

## 3:15–4:15 · Phản biện và giới hạn

Ticket hiểm ở B7.3: đơn quà O-1026 và khách khai 9 ngày dù DB 3 ngày. Kỳ vọng 20.000đ, đúng GHSH/3 ngày, thông báo không còn recipient_contact/customer_note. Có thể chạy lệnh adhoc trong B7.3.

Không sửa tiêu chí/snapshot/v1 trong demo. Nếu thử đổi config phải trả đúng bản v2 rồi chạy lại eval/grade/collect. Không tự tạo lại report cũ.

Lòng tin là mô hình mock, không phải phỏng vấn người thật; quyền có thể thay đổi giữa kiểm và ghi, DB có thể chậm. Ghi chú model có thể mang thông số proposal trước khi gate sửa; đọc ledger/gate làm nguồn sự thật.

## 4:15–5:00 · Quyết định và điều kiện còn thiếu

V2 giữ **Cải tiến thêm**: ngưỡng số, integrity, visible, regression và monitor đã đạt. Cần xác minh nguồn quyền, ghi đồng thời, công suất và đồng thuận kiểm mẫu của người thật trước pilot. Nhóm đã khôi phục byte gốc và tải đủ thẻ để khớp manifest theo yêu cầu trưởng nhóm; việc tải đủ thẻ khác hướng dẫn ban đầu, đã khai báo và chưa có xác nhận ngoại lệ của Coach. Hồ sơ đủ thành phần và PASS-VISIBLE chưa bảo đảm điểm/test ẩn.

Trước Gate 2: xác minh đồng bộ/cấp thu hồi quyền, an toàn giao dịch đồng thời, audit tiền, lưu lượng giờ cao điểm, chi phí theo kho, log và người duyệt thật có hiểu/đồng ý kiểm mẫu hay không.


## Cập nhật kiểm toàn vẹn · 18/11/2026

Theo yêu cầu trực tiếp của trưởng nhóm, đã tải đủ file gốc S1–S8 từ repo cards minhhai203 chỉ để khớp manifest; không sử dụng nội dung S1–S7 để thiết kế hay đánh giá giải pháp S8. Thao tác này khác hướng dẫn ban đầu chỉ nhận S8, được ghi minh bạch, chưa nhận xác nhận ngoại lệ từ Coach. Khôi phục LF cho19 file khóa đề và4 file S8 bằng cách kiểm SHA-256 đích trước khi ghi; không sửa logic, manifest, grader, tiêu chí hoặc snapshot. Thêm .gitattributes để giữ LF cho file khóa khi checkout.

Grade mới **R-S8-grade-20261118-174256-726304**: **PASS-VISIBLE (chưa chạy test ẩn)**. Integrity/criteria/visible/regression/monitor đều true, changed=[]; cả51 file khớp manifest. Các báo cáo FAIL trước đó được giữ làm lịch sử, không sửa. Ba mốc mới: base R-S8-before-20261118-174257-726304, prepared R-S8-prepared-20261118-174257-726304, after R-S8-after-20261118-174257-726304.

Không tự đổi quyết định v2: vẫn Cải tiến thêm vì cần xác minh người thật, quyền cập nhật/thu hồi và vận hành trước pilot thật; integrity không còn là lý do chặn ở lần chạy mới. Hồ sơ đạt visible không phải bảo đảm điểm rubric/test ẩn, và việc tải đủ thẻ cần được giải thích trung thực khi Coach hỏi.
