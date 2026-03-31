# SRS Group F - Validation Pack

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source SRS groups: `group-a` đến `group-e`

## 2. Test Cases

| TC ID | Objective | Linked Stories | Linked FR | Linked UC | Linked SCR |
| --- | --- | --- | --- | --- | --- |
| `TC-01` | Chọn vị trí pallet và nạp đúng cấu hình pallet | `US-01` | `FR-01`, `FR-02` | `UC-01` | `SCR-01` |
| `TC-02` | Chọn một `Carton Code` từ catalog và tự nạp kích thước | `US-02` | `FR-03`, `FR-06` | `UC-01` | `SCR-01` |
| `TC-03` | Chọn nhiều loại box trong cùng request | `US-02`, `US-03` | `FR-04`, `FR-05` | `UC-01` | `SCR-01` |
| `TC-04` | Chặn submit khi quantity không hợp lệ hoặc thiếu pallet | `US-04` | `FR-07` | `UC-01` | `SCR-01` |
| `TC-05` | Tạo baseline layout hợp lệ từ request đúng | `US-05` | `FR-08`, `FR-09` | `UC-02` | `SCR-01`, `SCR-02`, `SCR-03` |
| `TC-06` | Hiển thị `utilization` và `layer count` sau auto-pack | `US-06` | `FR-16` | `UC-02` | `SCR-03` |
| `TC-07` | Zoom và rotate 3D workspace không làm mất layout | `US-07` | `FR-10`, `FR-11` | `UC-03` | `SCR-02` |
| `TC-08` | Chọn box và xem thông tin selection detail | `US-08` | `FR-12` | `UC-03` | `SCR-02` |
| `TC-09` | Kéo box tạo layout mới và revalidate thành công | `US-09`, `US-11` | `FR-13`, `FR-15` | `UC-04` | `SCR-02`, `SCR-03` |
| `TC-10` | Xoay box tạo cảnh báo hoặc lỗi khi bất hợp lệ | `US-10`, `US-11` | `FR-14`, `FR-15` | `UC-04` | `SCR-02`, `SCR-03` |
| `TC-11` | Hiển thị invalid state và issue list sau manual change lỗi | `US-11` | `FR-15`, `FR-16` | `UC-04` | `SCR-03` |
| `TC-12` | Reset layout về baseline auto-pack | `US-12` | `FR-17` | `UC-05` | `SCR-03`, `SCR-02` |

## 3. Glossary

| Term | Definition |
| --- | --- |
| `Pallet Position` | Vị trí pallet được chọn trong kho, quyết định kích thước và giới hạn chiều cao áp dụng |
| `Carton Code` | Mã box chuẩn trong catalog master |
| `Box Catalog` | Danh mục box chuẩn với kích thước và metadata logistics |
| `Packing Request` | Payload gồm pallet position và box items gửi sang auto-packing |
| `Layout Baseline` | Kết quả auto-pack đầu tiên trước khi có manual change |
| `Manual Change` | Thao tác kéo thả hoặc xoay box trong workspace |
| `Validation State` | Trạng thái hợp lệ hiện hành của layout: `valid`, `warning`, `invalid` |
| `Utilization` | Tỷ lệ sử dụng thể tích pallet của layout hiện hành |
| `Layer Count` | Số lớp box trong layout |

## 4. Traceability Cross-references

### 4.1 Story To UC And Screen

| Story ID | UC | Screen |
| --- | --- | --- |
| `US-01` | `UC-01` | `SCR-01` |
| `US-02` | `UC-01` | `SCR-01` |
| `US-03` | `UC-01` | `SCR-01` |
| `US-04` | `UC-01` | `SCR-01` |
| `US-05` | `UC-02` | `SCR-01`, `SCR-02`, `SCR-03` |
| `US-06` | `UC-02` | `SCR-03` |
| `US-07` | `UC-03` | `SCR-02` |
| `US-08` | `UC-03` | `SCR-02` |
| `US-09` | `UC-04` | `SCR-02`, `SCR-03` |
| `US-10` | `UC-04` | `SCR-02`, `SCR-03` |
| `US-11` | `UC-04` | `SCR-03` |
| `US-12` | `UC-05` | `SCR-03`, `SCR-02` |

### 4.2 FR To Story To Screen

| FR ID | Stories | Screens |
| --- | --- | --- |
| `FR-01` | `US-01` | `SCR-01` |
| `FR-02` | `US-01` | `SCR-01` |
| `FR-03` | `US-02` | `SCR-01` |
| `FR-04` | `US-02`, `US-03` | `SCR-01` |
| `FR-05` | `US-03` | `SCR-01` |
| `FR-06` | `US-02` | `SCR-01` |
| `FR-07` | `US-04` | `SCR-01` |
| `FR-08` | `US-05` | `SCR-01`, `SCR-02`, `SCR-03` |
| `FR-09` | `US-05` | `SCR-03` |
| `FR-10` | `US-07` | `SCR-02` |
| `FR-11` | `US-07` | `SCR-02` |
| `FR-12` | `US-08` | `SCR-02` |
| `FR-13` | `US-09` | `SCR-02` |
| `FR-14` | `US-10` | `SCR-02` |
| `FR-15` | `US-09`, `US-10`, `US-11` | `SCR-02`, `SCR-03` |
| `FR-16` | `US-06`, `US-11` | `SCR-03` |
| `FR-17` | `US-12` | `SCR-03` |

