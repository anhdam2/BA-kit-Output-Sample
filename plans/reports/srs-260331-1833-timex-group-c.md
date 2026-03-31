# SRS Group C - Screen Contract Lite

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source use cases: `plans/reports/srs-260331-1833-timex-group-b.md`

## 2. Screen Inventory

| Screen ID | Screen name | Type | Linked UC | Linked stories | Purpose |
| --- | --- | --- | --- | --- | --- |
| `SCR-01` | Input cấu hình pallet và box | Primary | `UC-01`, `UC-02` | `US-01` đến `US-05` | Chuẩn bị request hợp lệ và kích hoạt auto-packing |
| `SCR-02` | 3D packing workspace | Primary | `UC-02`, `UC-03`, `UC-04` | `US-05`, `US-07` đến `US-10` | Quan sát trực quan layout và thao tác chỉnh tay |
| `SCR-03` | Kết quả và validation | Primary | `UC-02`, `UC-04`, `UC-05` | `US-05`, `US-06`, `US-09` đến `US-12` | Trình bày metric, trạng thái hợp lệ, và recovery actions |

## 3. Screen Contract Lite

### SCR-01 Input cấu hình pallet và box

| Contract Field | Value |
| --- | --- |
| Screen type | Primary |
| Entry condition | Người dùng mở app mới hoặc quay lại sau reset flow |
| Exit condition | Request hợp lệ được gửi sang auto-packing hoặc người dùng vẫn ở lại để sửa lỗi |
| Linked use cases | `UC-01`, `UC-02` |
| Linked stories | `US-01`, `US-02`, `US-03`, `US-04`, `US-05` |

Key actions:

- Chọn vị trí pallet.
- Xem kích thước pallet và giới hạn chiều cao.
- Tìm và chọn `Carton Code` từ catalog.
- Nhập số lượng theo từng loại box.
- Xóa box item khỏi request hiện hành.
- Chạy auto-packing.

Required states:

- `default-empty`: chưa chọn pallet và chưa có box item.
- `editing-valid`: request đang hợp lệ và có thể chạy.
- `validation-error`: tồn tại lỗi bắt buộc hoặc lỗi số lượng.
- `loading-pack`: đang gửi request và chờ kết quả.

### SCR-02 3D packing workspace

| Contract Field | Value |
| --- | --- |
| Screen type | Primary |
| Entry condition | Có layout hiện hành từ auto-pack hoặc manual update |
| Exit condition | Người dùng quay lại input, chuyển sang màn hình kết quả, hoặc kết thúc phiên |
| Linked use cases | `UC-02`, `UC-03`, `UC-04` |
| Linked stories | `US-05`, `US-07`, `US-08`, `US-09`, `US-10` |

Key actions:

- Zoom camera.
- Rotate camera.
- Chọn box.
- Kéo thả box đã chọn.
- Xoay box đã chọn.

Required states:

- `workspace-ready`: hiển thị đầy đủ pallet và placements.
- `box-selected`: có box đang được highlight và panel chi tiết hiển thị.
- `manual-dragging`: box đang được reposition.
- `invalid-layout-warning`: layout hiện hành có lỗi sau chỉnh tay.
- `renderer-error`: không tải được canvas hoặc dữ liệu layout.

### SCR-03 Kết quả và validation

| Contract Field | Value |
| --- | --- |
| Screen type | Primary |
| Entry condition | Có baseline layout từ auto-pack hoặc kết quả revalidation sau chỉnh tay |
| Exit condition | Người dùng chấp nhận layout, reset về baseline, hoặc quay lại input |
| Linked use cases | `UC-02`, `UC-04`, `UC-05` |
| Linked stories | `US-05`, `US-06`, `US-09`, `US-10`, `US-11`, `US-12` |

Key actions:

- Xem `space utilization`.
- Xem `layer count`.
- Xem `validation state`.
- Đọc danh sách issue hoặc warning nếu có.
- Reset về auto-pack baseline.
- Mở lại workspace 3D để tiếp tục chỉnh tay.

Required states:

- `auto-pack-success`: baseline hợp lệ sau auto-pack.
- `warning-state`: có cảnh báo nhưng vẫn hiển thị layout.
- `invalid-after-manual`: layout không hợp lệ sau chỉnh tay.
- `empty-or-failed`: không có layout hoặc auto-pack thất bại.

