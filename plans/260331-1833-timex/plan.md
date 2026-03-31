# BA Work Plan

## 1. Thông tin kế hoạch

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Mode: `hybrid`
- Ngôn ngữ deliverable: Tiếng Việt
- UI baseline mặc định: Shadcn UI

## 2. Scope đã khóa

- POC web app cho nhân viên kho.
- Bài toán chính: đề xuất cách xếp nhiều loại hộp vào pallet bằng 3D visualization và auto-packing.
- Có danh mục box chuẩn theo `Carton Code` với kích thước cố định từ dữ liệu nghiệp vụ.
- Cho phép chỉnh tay bằng kéo thả và xoay box.
- Pallet cố định theo vị trí, với giới hạn chiều cao khác nhau theo deck.

## 3. Deliverable selection

| Deliverable | Trạng thái | Lý do |
| --- | --- | --- |
| Intake | Bắt buộc | Đã có input thô và đã khóa scope |
| Requirements Backbone | Bắt buộc | Là nguồn sự thật chính cho các bước sau |
| FRD | Có | Cần mô tả feature, workflow, business rules cho handoff POC |
| User Stories | Có | Cần cho development theo flow và acceptance criteria |
| SRS chọn lọc | Có | Có UI, có 3D interaction, có auto-packing logic và metric validation |
| Wireframes | Có | Có UI-backed screens và workspace 3D cần mô tả rõ |
| Package | Có | Cần HTML stakeholder-facing cho bộ POC BA |

## 4. Hướng xử lý theo mode hybrid

### Backbone

- Chốt goals, feature map, FR/NFR sơ bộ, assumptions, gates.

### FRD

- Tài liệu ngắn gọn theo hướng POC.
- Tập trung vào:
  - input workflow và box catalog workflow
  - pallet selection logic
  - packing generation
  - 3D interaction
  - validation metrics

### User Stories

- Tổ chức theo các epic:
  - Quản lý box catalog, input box và pallet
  - Sinh phương án packing
  - Trực quan 3D và chỉnh sửa tay
  - Validation kết quả

### SRS chọn lọc

- Ưu tiên chi tiết cho:
  - cơ chế chọn box từ catalog chuẩn
  - quy tắc validate input
  - luồng sinh đề xuất
  - tương tác 3D
  - màn hình workspace
  - metric utilization và layering

### Wireframes

- Wireframe cho các màn hình lõi:
  - SCR-01 Input cấu hình
  - SCR-02 3D workspace
  - SCR-03 Kết quả và validation

## 5. Đề xuất agent ownership

| Agent | Slice |
| --- | --- |
| `requirements-engineer` | Backbone, FRD, user stories, SRS core |
| `ui-ux-designer` | Wireframe cho flow input và 3D workspace |
| `ba-documentation-manager` | Quality review, packaging, traceability |
| `ba-researcher` | Nghiên cứu heuristic packing và lựa chọn 3D visualization nếu cần |

## 6. Rủi ro và lưu ý

- Chưa có KPI định lượng cuối cùng cho utilization và thời gian xử lý.
- Chưa xác nhận đầy đủ decision maker nghiệp vụ.
- Chưa khóa việc POC có cho nhập box ngoài catalog chuẩn hay không.
- Chưa khóa quy tắc input số lượng box theo loại.
- Chưa xác định volume weight và freight cost sẽ chỉ hiển thị tham chiếu hay có tác động tới logic đề xuất.
- 3D manipulation trên web POC cần cân bằng giữa đơn giản triển khai và trải nghiệm đủ dùng.

## 7. Execution order

```text
Intake
-> Backbone
-> FRD
-> User Stories
-> Selective SRS
-> Wireframes
-> Package
```

## 8. Điều kiện hoàn thành intake phase

- Intake artifact được ghi ra Markdown và HTML.
- Scope POC được khóa rõ in-scope / out-of-scope.
- Kế hoạch deliverable cho mode `hybrid` được xác nhận.
- Các open question còn lại được ghi nhận để xử lý ở backbone thay vì chặn intake.
