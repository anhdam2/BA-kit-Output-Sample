# Wireframe Input Pack

## 1. Artifact Set Information

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- App type: Web app POC cho nhân viên kho
- Design baseline: Shadcn UI wireframe style
- Source use cases: `plans/reports/srs-260331-1833-timex-group-b.md`
- Source screen contract: `plans/reports/srs-260331-1833-timex-group-c.md`

## 2. Primary Screen Set

- `SCR-01` Input cấu hình pallet và box
- `SCR-02` 3D packing workspace
- `SCR-03` Kết quả và validation

## 3. Exact Use Case Excerpts Needed For Wireframes

### SCR-01

- Từ `UC-01`: chọn vị trí pallet, nạp pallet config, chọn nhiều `Carton Code`, nhập số lượng, validate lỗi ngay tại dòng, chặn auto-pack khi request chưa hợp lệ.
- Từ `UC-02`: thao tác `Run Auto-packing` được kích hoạt từ màn hình input và cần trạng thái `loading-pack`.

### SCR-02

- Từ `UC-02`: workspace nhận baseline layout sau auto-pack.
- Từ `UC-03`: cần `zoom`, `rotate`, chọn box, panel chi tiết khi box được chọn.
- Từ `UC-04`: cần thể hiện thao tác kéo thả, xoay box và trạng thái cảnh báo khi layout không hợp lệ.

### SCR-03

- Từ `UC-02`: cần `utilization`, `layer count`, `validation state` từ baseline layout.
- Từ `UC-04`: cần phản ánh kết quả revalidation sau chỉnh tay và danh sách warning/error.
- Từ `UC-05`: cần action `Reset to Auto-pack` và trạng thái disabled khi chưa có manual change.

## 4. Screen Contract Lite Summary

| Screen ID | Key actions | Required states |
| --- | --- | --- |
| `SCR-01` | chọn pallet, chọn `Carton Code`, nhập số lượng, chạy auto-pack | `default-empty`, `editing-valid`, `validation-error`, `loading-pack` |
| `SCR-02` | zoom, rotate, select, drag, rotate box | `workspace-ready`, `box-selected`, `manual-dragging`, `invalid-layout-warning`, `renderer-error` |
| `SCR-03` | xem metric, xem trạng thái, reset baseline, quay lại workspace | `auto-pack-success`, `warning-state`, `invalid-after-manual`, `empty-or-failed` |

## 5. Proposed Artifact Grouping Plan

### Artifact 1: `designs/timex/core-flow.pen`

Contains:

- Primary frame `SCR-01-input-config`
- Supporting frame `SCR-01-input-invalid`
- Primary frame `SCR-02-3d-workspace`
- Supporting frame `SCR-02-selection-warning`
- Primary frame `SCR-03-results-validation`
- Supporting frame `SCR-03-invalid-state`

Export targets:

- `designs/timex/exports/core-flow/SCR-01-input-config.png`
- `designs/timex/exports/core-flow/SCR-02-3d-workspace.png`
- `designs/timex/exports/core-flow/SCR-03-results-validation.png`

## 6. Stop Conditions

- Dừng nếu `SCR-01`, `SCR-02`, `SCR-03` không còn giữ cùng terminology với `UC` và `US`.
- Dừng nếu thiếu state ảnh hưởng trực tiếp đến flow chính: validation error, loading, box-selected, invalid-after-manual.
- Dừng nếu wireframe chỉ mô tả mỹ thuật mà không đủ vùng thông tin cho field tables và traceability.

