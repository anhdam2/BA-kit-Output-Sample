# SRS Group E - Final Screen Descriptions

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source use cases: `plans/reports/srs-260331-1833-timex-group-b.md`
- Source screen contract: `plans/reports/srs-260331-1833-timex-group-c.md`
- Wireframe map: `plans/reports/wireframe-map-260331-1833-timex.md`

## 2. Screen Descriptions

### SCR-01 Input cấu hình pallet và box

Linked:

- Use cases: `UC-01`, `UC-02`
- Stories: `US-01`, `US-02`, `US-03`, `US-04`, `US-05`
- Wireframe: `designs/timex/core-flow.pen#SCR-01-input-config`
- Export: `../../designs/timex/exports/core-flow/SCR-01-input-config.png`

![SCR-01 Input cấu hình pallet và box](../../designs/timex/exports/core-flow/SCR-01-input-config.png)

Layout regions:

- Header: tên màn hình, mô tả ngắn, trạng thái request hiện hành.
- Left panel: pallet context, selected box items, validation preview, CTA chạy auto-pack.
- Right panel: box catalog master và khu vực tìm kiếm/chọn `Carton Code`.

User actions:

- Chọn pallet position.
- Tìm `Carton Code`.
- Thêm box vào request.
- Nhập hoặc sửa quantity.
- Xóa box item khỏi request.
- Bấm `Run Auto-packing`.

System behaviour:

- Nạp kích thước pallet ngay sau khi chọn pallet position.
- Tự nạp kích thước box khi chọn `Carton Code`.
- Validate line-level và form-level trước khi cho phép chạy.
- Hiển thị `loading-pack` khi request đang gửi sang auto-packing.

States:

- `default-empty`
- `editing-valid`
- `validation-error`
- `loading-pack`

| Field Name | Field Type | Description |
| --- | --- | --- |
| Pallet Position | Select | Display: hiển thị danh sách vị trí pallet hỗ trợ. / Behaviour: khi đổi giá trị phải nạp lại cấu hình pallet. / Validation: bắt buộc trước khi chạy auto-pack. |
| Pallet Length | Read-only metric card | Display: hiển thị chiều dài pallet theo `cm`. / Behaviour: cập nhật ngay khi đổi pallet position. |
| Pallet Width | Read-only metric card | Display: hiển thị chiều rộng pallet theo `cm`. / Behaviour: cập nhật ngay khi đổi pallet position. |
| Max Height | Read-only metric card | Display: hiển thị chiều cao tối đa theo vị trí pallet. / Behaviour: dùng làm ràng buộc cho packing engine. |
| Catalog Search | Search input | Display: cho phép tìm theo `Carton Code` hoặc mô tả. / Behaviour: filter danh sách catalog theo text nhập. |
| Catalog Result Row | Selectable row | Display: hiển thị `Carton Code`, kích thước chuẩn, `volume weight`, `annual volume`. / Behaviour: thao tác `Add` thêm box vào danh sách đã chọn. |
| Selected Box Item Row | Composite row | Display: hiển thị `Carton Code`, kích thước chuẩn, quantity, action remove. / Behaviour: update quantity theo từng dòng. / Validation: quantity phải là số nguyên dương. |
| Validation Banner | Inline alert | Display: hiển thị lỗi tổng hợp khi request chưa hợp lệ. / Behaviour: xuất hiện khi có lỗi form-level hoặc line-level chưa xử lý xong. |
| Run Auto-packing | Primary button | Display: trạng thái enabled hoặc disabled theo tính hợp lệ của request. / Behaviour: gửi request sang `UC-02`. / Validation: không cho submit khi thiếu pallet position hoặc box items hợp lệ. |

### SCR-02 3D packing workspace

Linked:

- Use cases: `UC-02`, `UC-03`, `UC-04`
- Stories: `US-05`, `US-07`, `US-08`, `US-09`, `US-10`
- Wireframe: `designs/timex/core-flow.pen#SCR-02-3d-workspace`
- Export: `../../designs/timex/exports/core-flow/SCR-02-3d-workspace.png`

![SCR-02 3D packing workspace](../../designs/timex/exports/core-flow/SCR-02-3d-workspace.png)

Layout regions:

- Header: tên màn hình và toolbar camera/manual mode.
- Canvas card: vùng 3D chính hiển thị pallet, box, highlight selection.
- Side panel: box detail, manual actions, warning state.

User actions:

- Zoom camera.
- Rotate camera.
- Chọn box.
- Kéo box đã chọn.
- Xoay box đã chọn.

System behaviour:

- Tải layout hiện hành từ layout state store.
- Highlight box khi được chọn.
- Gửi layout mới sang validation engine sau drag hoặc rotate.
- Hiển thị warning khi layout mới không hợp lệ.

States:

- `workspace-ready`
- `box-selected`
- `manual-dragging`
- `invalid-layout-warning`
- `renderer-error`

| Field Name | Field Type | Description |
| --- | --- | --- |
| 3D Layout Canvas | Interactive viewport | Display: hiển thị pallet base và box placements theo perspective view. / Behaviour: hỗ trợ zoom, rotate, select. / Validation: empty state nếu chưa có layout. |
| Camera Controls | Toolbar chips/buttons | Display: hiển thị các thao tác `Zoom` và `Rotate`. / Behaviour: cập nhật góc nhìn nhưng không đổi layout data. |
| Selected Box Detail | Read-only detail card | Display: hiển thị `layout_box_id`, `carton_code`, layer, orientation, position. / Behaviour: thay đổi theo box đang selected. |
| Drag Selected Box | Action button/gesture handle | Display: chỉ meaningful khi đang có box được chọn. / Behaviour: bật chế độ reposition. / Validation: phải revalidate sau khi thả box. |
| Rotate Selected Box | Action button | Display: chỉ meaningful khi đang có box được chọn. / Behaviour: đổi orientation theo rule POC. / Validation: phải revalidate sau khi xoay. |
| Invalid Layout Warning | Warning card | Display: hiện cảnh báo khi layout sau chỉnh tay bị overlap, out-of-bound, hoặc vượt max height. / Behaviour: không tự động xác nhận layout hợp lệ cho đến khi revalidation pass. |

### SCR-03 Kết quả và validation

Linked:

- Use cases: `UC-02`, `UC-04`, `UC-05`
- Stories: `US-05`, `US-06`, `US-09`, `US-10`, `US-11`, `US-12`
- Wireframe: `designs/timex/core-flow.pen#SCR-03-results-validation`
- Export: `../../designs/timex/exports/core-flow/SCR-03-results-validation.png`

![SCR-03 Kết quả và validation](../../designs/timex/exports/core-flow/SCR-03-results-validation.png)

Layout regions:

- Header: tên màn hình và badge trạng thái.
- Summary row: metric cards cho `utilization`, `layer count`, `validation state`.
- Left content: issue list và diễn giải kết quả.
- Right action panel: mở workspace, reset baseline, note về disabled state.

User actions:

- Xem metric hiện hành.
- Xem validation state.
- Xem issue list hoặc warning.
- Mở lại 3D workspace.
- Reset về auto-pack baseline.

System behaviour:

- Đồng bộ metric mới nhất sau auto-pack hoặc manual revalidation.
- Hiển thị cảnh báo hoặc lỗi nếu layout không hợp lệ.
- Vô hiệu hóa `Reset to Auto-pack` khi chưa có manual change.

States:

- `auto-pack-success`
- `warning-state`
- `invalid-after-manual`
- `empty-or-failed`

| Field Name | Field Type | Description |
| --- | --- | --- |
| Space Utilization | Metric card | Display: hiển thị phần trăm sử dụng thể tích. / Behaviour: cập nhật sau mọi lần revalidation. |
| Layer Count | Metric card | Display: hiển thị số layer của layout hiện hành. / Behaviour: cập nhật từ cùng nguồn layout state với utilization. |
| Validation State | Status card/badge | Display: `Valid`, `Warning`, hoặc `Invalid`. / Behaviour: phản ánh kết quả validation engine. |
| Result Interpretation | Rich text panel | Display: tóm tắt chất lượng layout và các rule pass/fail chính. / Behaviour: thay đổi theo trạng thái hiện hành. |
| Issue List | List panel | Display: liệt kê overlap, out-of-bound, height overflow, hoặc warning cần chú ý. / Behaviour: rỗng khi layout hợp lệ hoàn toàn. |
| Open 3D Workspace | Secondary action | Display: luôn hiện khi có layout. / Behaviour: điều hướng quay lại `SCR-02`. |
| Reset to Auto-pack | Primary action | Display: enabled khi đã có manual change; disabled hoặc hidden nếu chưa có manual change. / Behaviour: gọi `UC-05` để phục hồi baseline. |

