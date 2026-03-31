# Wireframe Map

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Input pack: `plans/reports/wireframe-input-260331-1833-timex.md`
- Artifact: `designs/timex/core-flow.pen`

## 2. Screen To Artifact Mapping

| Screen ID | Linked UC | Artifact | Primary frame | Supporting frames | Export path | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| `SCR-01` | `UC-01`, `UC-02` | `designs/timex/core-flow.pen` | `SCR-01-input-config` | `SCR-01-input-invalid` | `designs/timex/exports/core-flow/SCR-01-input-config.png` | Làm rõ pallet context, selected items, catalog-first workflow và validation preview |
| `SCR-02` | `UC-02`, `UC-03`, `UC-04` | `designs/timex/core-flow.pen` | `SCR-02-3d-workspace` | `SCR-02-selection-warning` | `designs/timex/exports/core-flow/SCR-02-3d-workspace.png` | Thể hiện canvas 3D, chọn box, manual actions, warning state sau chỉnh tay |
| `SCR-03` | `UC-02`, `UC-04`, `UC-05` | `designs/timex/core-flow.pen` | `SCR-03-results-validation` | `SCR-03-invalid-state` | `designs/timex/exports/core-flow/SCR-03-results-validation.png` | Thể hiện metric, validation state, issue list và reset action |

## 3. Verification Notes

- `SCR-01` screenshot xác nhận được vùng nhập context, bảng item, catalog và CTA chính.
- `SCR-02` screenshot xác nhận được canvas chính, selection state và side panel cho manual adjustment.
- `SCR-03` screenshot xác nhận được metric cards, issue panel và action panel.
- Tất cả export PNG primary screens đã được ghi đúng dưới `designs/timex/exports/core-flow/`.

