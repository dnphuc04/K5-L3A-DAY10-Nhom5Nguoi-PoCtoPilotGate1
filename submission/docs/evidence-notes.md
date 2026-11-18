# Giới hạn và nguồn bằng chứng

- Báo cáo và journal trong bài nộp được thu từ các lần chạy thực tế trên máy Phúc và bản gốc Hoàng bàn giao. Thư mục runs/original-evidence giữ các bằng chứng bổ sung; không sửa số hoặc thời gian báo cáo.
- Đã bổ sung bản gốc của Hoàng từ thư mục Downloads/runs: `R-base-after-20261118-160422-0cb2ae` và `R-base-after-20261118-160436-2a7275`, gồm report.json và toàn bộ traces/, tại `submission/runs/original-evidence/`. Nhật ký gốc giữ nguyên tại `hoang-journal.jsonl`; các dòng chưa có được bổ sung vào journal chung, không ghi đè nhật ký máy Phúc. Kiểm SHA-256 xác nhận các file sao chép khớp nguồn; chi phí/ROI trong hai report lần lượt 4.457đ/1,2 và 5.821đ/0,69, khớp số liệu Phiếu B. Theo xác nhận của trưởng nhóm ngày 18/11/2026, trong quá trình làm bài Hưng đã lỡ xóa file gốc của lần chạy `R-base-after-20261118-161730-6f4f66` và không khôi phục được. Số liệu đã ghi trong Phiếu B được giữ nguyên, nhưng không còn report gốc để đối chiếu độc lập. Các report tích hợp cuối của nhóm vẫn được lưu đầy đủ; không dùng chúng thay cho chứng cứ của lần chạy cũ, không tái tạo report hoặc gán mã cũ cho lần chạy mới.
- Integrity FAIL: 19 file khóa đề +4 file S8 khớp manifest khi chuẩn hóa CRLF→LF trong bộ nhớ; core.autocrlf=true. Manifest còn yêu cầu28 file S1–S7 không được giao. Chưa sửa nội dung/line ending file khóa, manifest, bộ chấm, tiêu chí hay snapshot. Chưa có hướng dẫn Coach được ghi nhận. ĐỦ THÀNH PHẦN không có nghĩa integrity đã đạt.
- Thứ tự B6 vòng1 không theo quy trình lý tưởng: code Hảo đã có trước lúc tổng hợp B6. Ghi trung thực, không sửa lịch sử để giả pre-mortem. V1 đã chốt trước nhận S8; grade S8 đầu được lưu trước mọi thay đổi monitor vòng2.
- AI được dùng để hoàn thiện theo yêu cầu trưởng nhóm; mục cá nhân có bằng chứng đóng góp đã commit; trưởng nhóm thông báo ngày 18/11/2026 rằng cả nhóm đã tự rà soát và xác nhận mục cá nhân/exit ticket. Không giả chữ ký, họp nhóm, phỏng vấn hoặc liên hệ Coach/đối tác.
- Test ẩn chưa chạy; không tuyên bố đạt. V2 giữ Cải tiến thêm cho tới khi các điều kiện chưa đạt được giải quyết.


## Cập nhật kiểm toàn vẹn · 18/11/2026

Theo yêu cầu trực tiếp của trưởng nhóm, đã tải đủ file gốc S1–S8 từ repo cards minhhai203 chỉ để khớp manifest; không sử dụng nội dung S1–S7 để thiết kế hay đánh giá giải pháp S8. Thao tác này khác hướng dẫn ban đầu chỉ nhận S8, được ghi minh bạch, chưa nhận xác nhận ngoại lệ từ Coach. Khôi phục LF cho19 file khóa đề và4 file S8 bằng cách kiểm SHA-256 đích trước khi ghi; không sửa logic, manifest, grader, tiêu chí hoặc snapshot. Thêm .gitattributes để giữ LF cho file khóa khi checkout.

Grade mới **R-S8-grade-20261118-174256-726304**: **PASS-VISIBLE (chưa chạy test ẩn)**. Integrity/criteria/visible/regression/monitor đều true, changed=[]; cả51 file khớp manifest. Các báo cáo FAIL trước đó được giữ làm lịch sử, không sửa. Ba mốc mới: base R-S8-before-20261118-174257-726304, prepared R-S8-prepared-20261118-174257-726304, after R-S8-after-20261118-174257-726304.

Không tự đổi quyết định v2: vẫn Cải tiến thêm vì cần xác minh người thật, quyền cập nhật/thu hồi và vận hành trước pilot thật; integrity không còn là lý do chặn ở lần chạy mới. Hồ sơ đạt visible không phải bảo đảm điểm rubric/test ẩn, và việc tải đủ thẻ cần được giải thích trung thực khi Coach hỏi.
