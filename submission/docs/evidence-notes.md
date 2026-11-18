# Giới hạn và nguồn bằng chứng

- Báo cáo và journal trong bài nộp được chép từ lệnh chạy thực tế trên máy Phúc. Thư mục runs/original-evidence giữ thêm report lần đầu S8 và các report local sẵn có; không sửa số hoặc thời gian báo cáo.
- Các mã vòng1 của thành viên được trích trong Phiếu B (`R-base-after-20261118-160422-0cb2ae`, `R-base-after-20261118-160436-2a7275`, `R-base-after-20261118-161730-6f4f66`) chưa có file gốc trên máy Phúc. Phiếu B lưu số thành viên bàn giao; chưa xác minh lại report gốc. Không giả report/journal hoặc chạy lại rồi gán mã cũ. Cần bổ sung bản gốc từ người chạy nếu yêu cầu chứng cứ đầy đủ.
- Integrity FAIL: 19 file khóa đề +4 file S8 khớp manifest khi chuẩn hóa CRLF→LF trong bộ nhớ; core.autocrlf=true. Manifest còn yêu cầu28 file S1–S7 không được giao. Chưa sửa nội dung/line ending file khóa, manifest, bộ chấm, tiêu chí hay snapshot. Chưa có hướng dẫn Coach được ghi nhận. ĐỦ THÀNH PHẦN không có nghĩa integrity đã đạt.
- Thứ tự B6 vòng1 không theo quy trình lý tưởng: code Hảo đã có trước lúc tổng hợp B6. Ghi trung thực, không sửa lịch sử để giả pre-mortem. V1 đã chốt trước nhận S8; grade S8 đầu được lưu trước mọi thay đổi monitor vòng2.
- AI được dùng để hoàn thiện theo yêu cầu trưởng nhóm; mục cá nhân có bằng chứng đóng góp đã commit; trưởng nhóm thông báo ngày 18/11/2026 rằng cả nhóm đã tự rà soát và xác nhận mục cá nhân/exit ticket. Không giả chữ ký, họp nhóm, phỏng vấn hoặc liên hệ Coach/đối tác.
- Test ẩn chưa chạy; không tuyên bố đạt. V2 giữ Cải tiến thêm cho tới khi các điều kiện chưa đạt được giải quyết.


## Cập nhật kiểm toàn vẹn · 18/11/2026

Theo yêu cầu trực tiếp của trưởng nhóm, đã tải đủ file gốc S1–S8 từ repo cards minhhai203 chỉ để khớp manifest; không sử dụng nội dung S1–S7 để thiết kế hay đánh giá giải pháp S8. Thao tác này khác hướng dẫn ban đầu chỉ nhận S8, được ghi minh bạch, chưa nhận xác nhận ngoại lệ từ Coach. Khôi phục LF cho19 file khóa đề và4 file S8 bằng cách kiểm SHA-256 đích trước khi ghi; không sửa logic, manifest, grader, tiêu chí hoặc snapshot. Thêm .gitattributes để giữ LF cho file khóa khi checkout.

Grade mới **R-S8-grade-20261118-174256-726304**: **PASS-VISIBLE (chưa chạy test ẩn)**. Integrity/criteria/visible/regression/monitor đều true, changed=[]; cả51 file khớp manifest. Các báo cáo FAIL trước đó được giữ làm lịch sử, không sửa. Ba mốc mới: base R-S8-before-20261118-174257-726304, prepared R-S8-prepared-20261118-174257-726304, after R-S8-after-20261118-174257-726304.

Không tự đổi quyết định v2: vẫn Cải tiến thêm vì cần xác minh người thật, quyền cập nhật/thu hồi và vận hành trước pilot thật; integrity không còn là lý do chặn ở lần chạy mới. Hồ sơ đạt visible không phải bảo đảm điểm rubric/test ẩn, và việc tải đủ thẻ cần được giải thích trung thực khi Coach hỏi.
