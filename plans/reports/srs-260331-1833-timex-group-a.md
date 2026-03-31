# SRS Group A - Core

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Mode: `hybrid`
- Source backbone: `plans/reports/backbone-260331-1833-timex.md`
- Source user stories: `plans/reports/user-stories-260331-1833-timex.md`
- Source FRD: `plans/reports/frd-260331-1833-timex.md`
- Output language: Tiếng Việt

## 2. Purpose And Scope

### 2.1 Purpose

Tài liệu SRS này mô tả chọn lọc phạm vi POC của TimeX cho bài toán đề xuất xếp box lên pallet trong web app dành cho nhân viên kho. Mục tiêu của tài liệu là khóa rõ hành vi hệ thống, use case, screen contract, quy tắc kỹ thuật và traceability cần thiết để handoff implementation POC.

### 2.2 In-scope

- Chọn vị trí pallet và nạp thông số pallet cố định theo vị trí.
- Chọn box từ catalog chuẩn theo `Carton Code`.
- Nhập số lượng theo từng loại box.
- Validate dữ liệu đầu vào trước khi chạy packing.
- Sinh một phương án auto-packing ưu tiên `space utilization`.
- Hiển thị layout bằng 3D workspace.
- Hỗ trợ thao tác `zoom`, `rotate`, chọn box.
- Hỗ trợ chỉnh tay tối thiểu bằng kéo thả và xoay box.
- Hiển thị `space utilization`, `layer count`, và `validation state`.
- Hỗ trợ reset về layout auto-pack ban đầu nếu feature được bật trong POC.

### 2.3 Out-of-scope

- Tích hợp WMS, ERP, hoặc hệ thống hiện trường bên ngoài.
- Quản lý người dùng, phân quyền, lưu lịch sử, cộng tác thời gian thực.
- Tối ưu đa mục tiêu nâng cao dựa trên `volume weight`, `annual volume`, `annual volume weight`, hoặc `freight cost`.
- Cam kết hỗ trợ box ngoài catalog trong POC hiện tại.

## 3. Overall Description

### 3.1 Product Perspective

TimeX là web app POC chạy trên desktop browser hiện đại. Hệ thống nhận pallet context, danh sách box chuẩn và số lượng cần xếp, sau đó tạo layout gợi ý, cho phép người dùng kiểm tra bằng 3D workspace và chỉnh sửa ở mức tối thiểu.

### 3.2 User Class And Actors

| Actor | Type | Mục tiêu |
| --- | --- | --- |
| Nhân viên kho | Primary | Chuẩn bị dữ liệu, chạy packing, kiểm tra kết quả, chỉnh tay |
| Lead kho / vận hành | Secondary | Đánh giá tính phù hợp của layout và POC |
| Auto-packing service | System | Tính toán layout khả thi và metric nền |
| Validation engine | System | Kiểm tra layout sau auto-pack hoặc chỉnh tay |

### 3.3 Operating Assumptions

- Luồng chính dùng `catalog-first`.
- Người dùng thao tác trên desktop thay vì mobile.
- POC ưu tiên rõ ràng và tốc độ thao tác hơn chiều sâu tối ưu thuật toán.
- Dữ liệu pallet position và box catalog có thể seed tĩnh trong solution boundary.

### 3.4 Dependencies

- Danh sách vị trí pallet phải được seed và khóa trước UAT.
- Box catalog phải có dữ liệu kích thước nhất quán theo `Carton Code`.
- Auto-packing service và 3D workspace phải dùng chung schema layout.
- Metric `utilization` và `layer count` phải được tính từ cùng một nguồn layout state.

## 4. Functional Requirements Table

| FR ID | Requirement | Priority | Linked Stories | Linked Screens |
| --- | --- | --- | --- | --- |
| FR-01 | Hệ thống phải cho người dùng chọn vị trí pallet áp dụng. | Must | `US-01` | `SCR-01` |
| FR-02 | Hệ thống phải tự nạp kích thước pallet và giới hạn chiều cao theo vị trí đã chọn. | Must | `US-01` | `SCR-01` |
| FR-03 | Hệ thống phải cung cấp catalog box chuẩn theo `Carton Code`. | Must | `US-02` | `SCR-01` |
| FR-04 | Hệ thống phải cho phép chọn nhiều loại box trong cùng một lần tính toán. | Must | `US-02`, `US-03` | `SCR-01` |
| FR-05 | Hệ thống phải cho phép nhập số lượng theo từng loại box đã chọn. | Must | `US-03` | `SCR-01` |
| FR-06 | Hệ thống phải tự điền kích thước box từ catalog chuẩn khi người dùng chọn `Carton Code`. | Must | `US-02` | `SCR-01` |
| FR-07 | Hệ thống phải validate dữ liệu đầu vào trước khi chạy auto-packing. | Must | `US-04` | `SCR-01` |
| FR-08 | Hệ thống phải sinh phương án auto-packing khả thi trong giới hạn pallet. | Must | `US-05` | `SCR-01`, `SCR-02`, `SCR-03` |
| FR-09 | Hệ thống phải ưu tiên tối đa hóa sử dụng thể tích pallet trong phương án gợi ý. | Must | `US-05` | `SCR-03` |
| FR-10 | Hệ thống phải hiển thị kết quả packing ở dạng 3D. | Must | `US-07` | `SCR-02` |
| FR-11 | Hệ thống phải hỗ trợ `zoom` và `rotate` trong 3D workspace. | Must | `US-07` | `SCR-02` |
| FR-12 | Hệ thống phải cho phép chọn box trong 3D workspace. | Must | `US-08` | `SCR-02` |
| FR-13 | Hệ thống phải cho phép kéo thả box để chỉnh tay phương án xếp. | Should | `US-09` | `SCR-02` |
| FR-14 | Hệ thống phải cho phép xoay box khi chỉnh tay. | Should | `US-10` | `SCR-02` |
| FR-15 | Hệ thống phải cập nhật metric và trạng thái hợp lệ sau khi người dùng chỉnh tay. | Should | `US-09`, `US-10`, `US-11` | `SCR-02`, `SCR-03` |
| FR-16 | Hệ thống phải hiển thị tối thiểu các metric `space utilization` và `layer count`. | Must | `US-06`, `US-11` | `SCR-03` |
| FR-17 | Hệ thống nên cho phép reset phương án về kết quả auto-packing ban đầu. | Could | `US-12` | `SCR-03` |

## 5. Business Rules And Scope Locks

- BR-01: Người dùng phải chọn vị trí pallet trước khi chạy auto-packing.
- BR-02: Kích thước pallet và giới hạn chiều cao phải lấy từ `pallet_position` đã chọn.
- BR-03: Kích thước box phải lấy từ `box_catalog` theo `Carton Code`, không nhập tay trong luồng chính.
- BR-04: Số lượng box phải là số nguyên dương trong phạm vi hợp lệ của POC.
- BR-05: Layout không được vượt quá giới hạn chiều dài, chiều rộng, và chiều cao pallet.
- BR-06: `Utilization` là tiêu chí ưu tiên chính của layout auto-pack.
- BR-07: Sau chỉnh tay, hệ thống phải revalidate toàn bộ layout trước khi kết luận hợp lệ.
- BR-08: `Volume weight`, `annual volume`, `annual volume weight`, và `freight cost` chỉ là dữ liệu tham chiếu ở phạm vi SRS hiện tại.

