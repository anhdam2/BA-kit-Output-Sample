# User Stories

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source backbone: `plans/reports/backbone-260331-1833-timex.md`
- Source FRD: `plans/reports/frd-260331-1833-timex.md`
- Mode: `hybrid`
- Output language: Tiếng Việt

## 2. Epic Overview

| Epic ID | Epic | Mục tiêu |
| --- | --- | --- |
| EP-01 | Pallet Context And Box Input | Chuẩn bị dữ liệu đầu vào đúng và đủ để chạy packing |
| EP-02 | Auto-packing And Result Generation | Sinh phương án xếp ban đầu tối ưu theo utilization |
| EP-03 | 3D Visualization And Inspection | Cho phép người dùng quan sát và hiểu layout |
| EP-04 | Manual Adjustment And Revalidation | Cho phép chỉnh tay và kiểm tra lại tính hợp lệ |
| EP-05 | Recovery And Convenience | Hỗ trợ thao tác thuận tiện trong phạm vi POC |

## 3. User Stories

### EP-01. Pallet Context And Box Input

#### US-01 Chọn vị trí pallet

- Priority: Must
- Linked FR: `FR-01`, `FR-02`
- Linked Screens: `SCR-01`
- Story:
  As a nhân viên kho, I want to chọn vị trí pallet áp dụng so that hệ thống nạp đúng giới hạn không gian cho phương án xếp.

Acceptance Criteria:

- Given người dùng đang ở màn hình input, when chọn một vị trí pallet hợp lệ, then hệ thống hiển thị đúng cấu hình pallet tương ứng.
- Given vị trí pallet đã được chọn, when cấu hình pallet được nạp xong, then chiều dài, chiều rộng, và giới hạn chiều cao phải sẵn sàng cho bước packing.
- Given người dùng chưa chọn vị trí pallet, when cố chạy auto-packing, then hệ thống phải chặn thao tác và yêu cầu chọn vị trí pallet trước.

#### US-02 Chọn box từ catalog chuẩn

- Priority: Must
- Linked FR: `FR-03`, `FR-04`, `FR-06`
- Linked Screens: `SCR-01`
- Story:
  As a nhân viên kho, I want to chọn một hoặc nhiều `Carton Code` từ catalog box chuẩn so that tôi dùng đúng kích thước box được chuẩn hóa.

Acceptance Criteria:

- Given catalog box đã được nạp, when người dùng chọn một `Carton Code`, then hệ thống phải hiển thị đúng mô tả và kích thước chuẩn tương ứng.
- Given người dùng chọn nhiều `Carton Code`, when danh sách được cập nhật, then hệ thống phải giữ được từng loại box như các dòng riêng biệt.
- Given box được chọn từ catalog, when hệ thống hiển thị thông tin chi tiết, then người dùng không cần nhập lại chiều dài, rộng, cao bằng tay.

#### US-03 Nhập số lượng box theo loại

- Priority: Must
- Linked FR: `FR-04`, `FR-05`
- Linked Screens: `SCR-01`
- Story:
  As a nhân viên kho, I want to nhập số lượng cho từng loại box đã chọn so that hệ thống có đủ dữ liệu để tính toán phương án xếp.

Acceptance Criteria:

- Given danh sách box đã được chọn, when người dùng nhập số lượng cho từng loại, then hệ thống lưu được số lượng theo từng `Carton Code`.
- Given người dùng thay đổi số lượng của một loại box, when dữ liệu được cập nhật, then chỉ dòng tương ứng bị thay đổi.
- Given chưa có loại box nào được chọn, when người dùng cố nhập số lượng hoặc chạy packing, then hệ thống phải hướng dẫn chọn box trước.

#### US-04 Validate dữ liệu đầu vào

- Priority: Must
- Linked FR: `FR-07`
- Linked Screens: `SCR-01`
- Story:
  As a nhân viên kho, I want hệ thống validate dữ liệu đầu vào trước khi chạy packing so that tôi tránh tạo ra phương án từ dữ liệu sai.

Acceptance Criteria:

- Given vị trí pallet hoặc dữ liệu box còn thiếu, when người dùng chạy auto-packing, then hệ thống phải chặn và hiển thị lỗi rõ ràng.
- Given số lượng box không hợp lệ, when người dùng xác nhận thao tác, then hệ thống phải yêu cầu sửa dữ liệu trước khi tiếp tục.
- Given toàn bộ input hợp lệ, when người dùng chạy auto-packing, then hệ thống phải cho phép chuyển sang bước tính toán.

### EP-02. Auto-packing And Result Generation

#### US-05 Sinh phương án xếp tự động

- Priority: Must
- Linked FR: `FR-08`, `FR-09`
- Linked Screens: `SCR-01`, `SCR-02`, `SCR-03`
- Story:
  As a nhân viên kho, I want hệ thống sinh phương án xếp tự động so that tôi có điểm khởi đầu tốt mà không phải thử-sai hoàn toàn bằng tay.

Acceptance Criteria:

- Given dữ liệu đầu vào hợp lệ, when người dùng chạy auto-packing, then hệ thống phải trả về ít nhất một layout khả thi trong giới hạn pallet.
- Given layout được sinh, when hệ thống hoàn tất xử lý, then phương án không được vượt chiều dài, chiều rộng, hoặc chiều cao pallet.
- Given có nhiều cách đặt box khả thi trong phạm vi heuristic, when hệ thống chọn kết quả gợi ý, then phương án phải ưu tiên utilization cao hơn.

#### US-06 Xem metric kết quả

- Priority: Must
- Linked FR: `FR-16`
- Linked Screens: `SCR-03`
- Story:
  As a nhân viên kho, I want xem metric utilization và layer count so that tôi hiểu nhanh chất lượng phương án xếp.

Acceptance Criteria:

- Given auto-packing đã hoàn thành, when kết quả được hiển thị, then hệ thống phải hiển thị `space utilization`.
- Given auto-packing đã hoàn thành, when kết quả được hiển thị, then hệ thống phải hiển thị `layer count`.
- Given layout thay đổi sau chỉnh tay, when metric được làm mới, then màn hình kết quả phải phản ánh số liệu mới nhất.

### EP-03. 3D Visualization And Inspection

#### US-07 Quan sát layout 3D

- Priority: Must
- Linked FR: `FR-10`, `FR-11`
- Linked Screens: `SCR-02`
- Story:
  As a nhân viên kho, I want xem layout ở dạng 3D với zoom và rotate so that tôi hiểu trực quan cách các box nằm trong pallet.

Acceptance Criteria:

- Given layout đã được sinh, when người dùng mở 3D workspace, then hệ thống phải hiển thị pallet và các box trong không gian 3D.
- Given workspace đang mở, when người dùng thao tác zoom, then góc nhìn phải thay đổi tương ứng mà không làm mất layout.
- Given workspace đang mở, when người dùng xoay góc nhìn, then người dùng phải quan sát được layout từ nhiều hướng.

#### US-08 Chọn box để kiểm tra

- Priority: Must
- Linked FR: `FR-12`
- Linked Screens: `SCR-02`
- Story:
  As a nhân viên kho, I want chọn từng box trong 3D workspace so that tôi có thể kiểm tra vị trí và orientation của box đó.

Acceptance Criteria:

- Given layout đang hiển thị, when người dùng chọn một box, then box đó phải được nhận diện rõ trên workspace.
- Given một box đã được chọn, when trạng thái được hiển thị, then người dùng phải thấy được box đang ở vị trí nào trong layout.
- Given box được chọn, when người dùng chuyển sang box khác, then hệ thống phải cập nhật selection tương ứng.

### EP-04. Manual Adjustment And Revalidation

#### US-09 Kéo thả box để chỉnh tay

- Priority: Should
- Linked FR: `FR-13`, `FR-15`
- Linked Screens: `SCR-02`, `SCR-03`
- Story:
  As a nhân viên kho, I want kéo thả box trong workspace so that tôi có thể thử điều chỉnh layout theo quan sát thực tế.

Acceptance Criteria:

- Given một box đang được chọn, when người dùng kéo box sang vị trí khác, then hệ thống phải cập nhật layout theo thay đổi đó.
- Given box được kéo sang vị trí không hợp lệ, when thao tác kết thúc, then hệ thống phải phản ánh trạng thái không hợp lệ hoặc cảnh báo tương ứng.
- Given layout thay đổi do kéo thả, when hệ thống hoàn tất cập nhật, then metric và validation state phải được làm mới.

#### US-10 Xoay box khi cần điều chỉnh

- Priority: Should
- Linked FR: `FR-14`, `FR-15`
- Linked Screens: `SCR-02`, `SCR-03`
- Story:
  As a nhân viên kho, I want xoay box trong layout so that tôi có thể kiểm tra các cách sắp xếp khác nhau mà không cần nhập lại dữ liệu.

Acceptance Criteria:

- Given một box đang được chọn, when người dùng thực hiện lệnh xoay, then orientation của box phải được cập nhật trong layout.
- Given orientation mới làm layout không hợp lệ, when hệ thống kiểm tra xong, then trạng thái lỗi hoặc cảnh báo phải được hiển thị rõ.
- Given orientation mới hợp lệ, when layout được cập nhật, then metric kết quả phải phản ánh cấu hình mới.

#### US-11 Xem lại trạng thái hợp lệ sau chỉnh tay

- Priority: Should
- Linked FR: `FR-15`, `FR-16`
- Linked Screens: `SCR-03`
- Story:
  As a nhân viên kho, I want xem trạng thái hợp lệ sau mỗi lần chỉnh tay so that tôi biết layout hiện tại còn dùng được hay không.

Acceptance Criteria:

- Given người dùng vừa kéo thả hoặc xoay box, when hệ thống kiểm tra lại layout, then phải có validation state mới.
- Given layout hợp lệ, when trạng thái được hiển thị, then người dùng thấy rõ kết quả có thể chấp nhận.
- Given layout không hợp lệ, when trạng thái được hiển thị, then người dùng phải nhận biết được rằng cần chỉnh lại.

### EP-05. Recovery And Convenience

#### US-12 Reset về layout auto-pack ban đầu

- Priority: Could
- Linked FR: `FR-17`
- Linked Screens: `SCR-03`
- Story:
  As a nhân viên kho, I want reset layout về kết quả auto-pack ban đầu so that tôi có thể thử lại nhanh sau khi chỉnh tay không như mong muốn.

Acceptance Criteria:

- Given người dùng đã chỉnh tay layout, when chọn reset, then hệ thống khôi phục layout auto-pack ban đầu.
- Given reset hoàn tất, when màn hình được cập nhật, then 3D workspace và metric phải quay về trạng thái ban đầu của auto-pack.
- Given người dùng chưa chỉnh tay, when xem tùy chọn reset, then hệ thống có thể ẩn hoặc vô hiệu hóa thao tác này.

## 4. INVEST Validation

| Story ID | Independent | Negotiable | Valuable | Estimable | Small | Testable | Ghi chú |
| --- | --- | --- | --- | --- | --- | --- | --- |
| US-01 | Có | Có | Có | Có | Có | Có | Tách biệt khỏi luồng box catalog |
| US-02 | Có | Có | Có | Có | Có | Có | Có thể làm trước phần 3D |
| US-03 | Có | Có | Có | Có | Có | Có | Bám chặt vào catalog workflow |
| US-04 | Có | Có | Có | Có | Có | Có | Validation tách riêng để dễ test |
| US-05 | Có | Có | Có | Có | Vừa | Có | Story lõi của sản phẩm |
| US-06 | Có | Có | Có | Có | Có | Có | Metric hiển thị tách khỏi thuật toán |
| US-07 | Có | Có | Có | Có | Vừa | Có | Có phụ thuộc layout result |
| US-08 | Có | Có | Có | Có | Có | Có | Bổ sung cho workspace 3D |
| US-09 | Có | Có | Có | Có | Vừa | Có | POC scope ở mức Should |
| US-10 | Có | Có | Có | Có | Có | Có | Có thể thực hiện cùng manual adjustment layer |
| US-11 | Có | Có | Có | Có | Có | Có | Validation sau chỉnh tay |
| US-12 | Có | Có | Có | Có | Có | Có | Convenience feature, không chặn POC |

## 5. Story To Screen Alignment

| Story ID | Screen | Mục đích chính |
| --- | --- | --- |
| US-01 | `SCR-01` | Chọn vị trí pallet |
| US-02 | `SCR-01` | Chọn `Carton Code` từ catalog |
| US-03 | `SCR-01` | Nhập số lượng từng loại box |
| US-04 | `SCR-01` | Validate dữ liệu đầu vào |
| US-05 | `SCR-01`, `SCR-02`, `SCR-03` | Kích hoạt packing và nhận layout kết quả |
| US-06 | `SCR-03` | Xem utilization và layer count |
| US-07 | `SCR-02` | Quan sát layout 3D |
| US-08 | `SCR-02` | Chọn box và kiểm tra |
| US-09 | `SCR-02`, `SCR-03` | Kéo thả box và xem trạng thái mới |
| US-10 | `SCR-02`, `SCR-03` | Xoay box và xem trạng thái mới |
| US-11 | `SCR-03` | Xem validation state sau chỉnh tay |
| US-12 | `SCR-03` | Reset về layout auto-pack |

## 6. Story To Requirement Traceability

| Story ID | FR coverage |
| --- | --- |
| US-01 | `FR-01`, `FR-02` |
| US-02 | `FR-03`, `FR-04`, `FR-06` |
| US-03 | `FR-04`, `FR-05` |
| US-04 | `FR-07` |
| US-05 | `FR-08`, `FR-09` |
| US-06 | `FR-16` |
| US-07 | `FR-10`, `FR-11` |
| US-08 | `FR-12` |
| US-09 | `FR-13`, `FR-15` |
| US-10 | `FR-14`, `FR-15` |
| US-11 | `FR-15`, `FR-16` |
| US-12 | `FR-17` |

## 7. Recommended Downstream Use

- Dùng `US-01` đến `US-06` để dẫn hướng các use case cốt lõi trong SRS.
- Dùng `US-07` đến `US-11` để viết `Screen Contract Lite` cho `SCR-02` và `SCR-03`.
- Dùng `US-04`, `US-09`, `US-10`, `US-11` làm nguồn chính cho validation rules và state handling.
