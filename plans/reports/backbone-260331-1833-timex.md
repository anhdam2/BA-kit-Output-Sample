# Requirements Backbone

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source intake: `plans/reports/intake-timex-260331-1833.md`
- Engagement mode: `hybrid`
- Output language: Tiếng Việt
- Product stage: POC
- Platform: Web app
- UI baseline mặc định: Shadcn UI

## 2. Scope Lock Summary

### In-scope

- Web app POC cho nhân viên kho.
- Chọn pallet theo vị trí với thông số pallet cố định và giới hạn chiều cao theo deck.
- Quản lý input box nhiều loại với validate dữ liệu.
- Hỗ trợ catalog box chuẩn theo `Carton Code` và kích thước cố định.
- Sinh đề xuất auto-packing ưu tiên tối đa hóa sử dụng thể tích pallet.
- Hiển thị phương án xếp bằng mô hình 3D có `zoom`, `rotate`, chọn box.
- Cho phép chỉnh tay tối thiểu bằng kéo thả và xoay box.
- Hiển thị các metric lõi như `space utilization` và `layer count`.

### Out-of-scope

- Tích hợp WMS, ERP, hoặc hệ thống vận hành hiện hữu.
- Tối ưu đa mục tiêu nâng cao như trọng tâm tải, ràng buộc hàng dễ vỡ, hay quy tắc chất xếp đặc thù.
- Quản trị người dùng, phân quyền, audit log, đồng bộ thời gian thực.
- Bài toán tối ưu logistics sâu sử dụng `annual volume`, `volume weight`, hoặc `freight cost` làm objective chính.

### Scope decision

- POC đi theo hướng `catalog-first`: box chuẩn theo `Carton Code` là luồng chính.
- Khả năng nhập box ngoài catalog được giữ ở trạng thái mở và chưa xem là cam kết POC.

## 3. Business Goals And Success Metrics

### Business goals

- Tăng tỷ lệ sử dụng thể tích pallet.
- Giảm thời gian lập phương án xếp hàng.
- Giảm lỗi vận hành do hình dung không gian và thử-sai thủ công.

### Success metrics draft

| Goal | Metric draft | Trạng thái |
| --- | --- | --- |
| Tối ưu không gian | `% pallet utilization` theo thể tích | Chưa khóa target |
| Tăng tốc thao tác | Thời gian từ nhập dữ liệu đến có phương án xếp đầu tiên | Chưa khóa target |
| Giảm lỗi | Số lần cần sắp xếp lại thủ công hoặc số phương án không hợp lệ | Chưa khóa target |
| Khả năng dùng POC | Tỷ lệ chạy thành công với catalog box chuẩn | Có thể đo trong test/UAT |

### Success metric assumptions

- Trong POC, `utilization` là KPI chính.
- `Layer count` là metric giải thích kết quả, không phải objective tối ưu độc lập.
- `Volume weight`, `annual volume`, và `freight cost` hiện là dữ liệu tham chiếu cho phân tích nghiệp vụ, chưa bắt buộc đi vào thuật toán.

## 4. Actors

| Actor | Vai trò | Mục tiêu |
| --- | --- | --- |
| Nhân viên kho | Primary actor | Tạo và chỉnh phương án xếp pallet nhanh, dễ hiểu |
| Lead kho / vận hành | Reviewer / approver giả định | Đánh giá độ phù hợp của POC và đầu ra |
| Hệ thống auto-packing | System actor | Sinh phương án khởi tạo khả thi theo pallet và box input |

## 5. Feature Map

### F1. Pallet Context

- Chọn vị trí pallet.
- Tự nạp kích thước pallet và giới hạn chiều cao theo vị trí.
- Hiển thị thông tin pallet hiện hành để người dùng không nhập sai context.

### F2. Box Catalog And Input

- Hiển thị danh mục box chuẩn theo `Carton Code`.
- Cho phép chọn một hoặc nhiều loại box trong một phiên tính toán.
- Nhập số lượng theo từng loại box.
- Tự nạp kích thước box chuẩn từ catalog.
- Validate dữ liệu đầu vào trước khi chạy thuật toán.

### F3. Auto-packing

- Sinh phương án xếp ban đầu dựa trên pallet context và danh sách box.
- Tối đa hóa sử dụng không gian như objective chính.
- Bảo đảm phương án không vượt kích thước pallet và giới hạn chiều cao.
- Trả về cấu trúc xếp có thể hiển thị trong 3D workspace.

### F4. 3D Workspace

- Hiển thị box và pallet ở dạng 3D.
- Cho phép `zoom`, `rotate`, và chọn box.
- Phản ánh vị trí, layer và orientation của từng box.

### F5. Manual Adjustment

- Kéo thả box trong workspace.
- Xoay box.
- Cập nhật lại bố cục và trạng thái hợp lệ sau chỉnh sửa.

### F6. Result Validation

- Hiển thị `space utilization`.
- Hiển thị số `layer`.
- Hiển thị trạng thái hợp lệ/không hợp lệ sau auto-pack hoặc chỉnh tay.

## 6. FR Draft Inventory

| ID | Functional requirement draft | Priority |
| --- | --- | --- |
| FR-01 | Hệ thống phải cho người dùng chọn vị trí pallet áp dụng. | Must |
| FR-02 | Hệ thống phải tự nạp kích thước pallet và giới hạn chiều cao theo vị trí đã chọn. | Must |
| FR-03 | Hệ thống phải cung cấp catalog box chuẩn theo `Carton Code`. | Must |
| FR-04 | Hệ thống phải cho phép chọn nhiều loại box trong cùng một lần tính toán. | Must |
| FR-05 | Hệ thống phải cho phép nhập số lượng theo từng loại box đã chọn. | Must |
| FR-06 | Hệ thống phải tự điền kích thước box từ catalog chuẩn khi người dùng chọn `Carton Code`. | Must |
| FR-07 | Hệ thống phải validate dữ liệu đầu vào trước khi chạy auto-packing. | Must |
| FR-08 | Hệ thống phải sinh phương án auto-packing khả thi trong giới hạn pallet. | Must |
| FR-09 | Hệ thống phải ưu tiên tối đa hóa sử dụng thể tích pallet trong phương án gợi ý. | Must |
| FR-10 | Hệ thống phải hiển thị kết quả packing ở dạng 3D. | Must |
| FR-11 | Hệ thống phải hỗ trợ `zoom` và `rotate` trong 3D workspace. | Must |
| FR-12 | Hệ thống phải cho phép chọn box trong 3D workspace. | Must |
| FR-13 | Hệ thống phải cho phép kéo thả box để chỉnh tay phương án xếp. | Should |
| FR-14 | Hệ thống phải cho phép xoay box khi chỉnh tay. | Should |
| FR-15 | Hệ thống phải cập nhật metric và trạng thái hợp lệ sau khi người dùng chỉnh tay. | Should |
| FR-16 | Hệ thống phải hiển thị tối thiểu các metric `space utilization` và `layer count`. | Must |
| FR-17 | Hệ thống nên cho phép reset phương án về kết quả auto-packing ban đầu. | Could |
| FR-18 | Hệ thống có thể hỗ trợ nhập box ngoài catalog ở giai đoạn sau nếu POC cần. | Won't for current lock |

## 7. NFR Draft Inventory

| ID | Non-functional requirement draft | Priority |
| --- | --- | --- |
| NFR-01 | UI phải đủ đơn giản để nhân viên kho thao tác với training tối thiểu. | Must |
| NFR-02 | 3D visualization phải phản hồi mượt ở mức đủ dùng cho POC trên trình duyệt desktop hiện đại. | Must |
| NFR-03 | Hệ thống phải ngăn dữ liệu đầu vào sai định dạng hoặc vượt phạm vi hợp lệ. | Must |
| NFR-04 | Thuật toán phải trả kết quả trong thời gian hợp lý cho tập box POC. | Must |
| NFR-05 | Danh mục box chuẩn phải được quản lý nhất quán, không bị sửa sai ngoài chủ ý. | Must |
| NFR-06 | Tên field, đơn vị đo, và label phải nhất quán giữa input, result, và 3D workspace. | Must |
| NFR-07 | Hệ thống nên có kiến trúc đủ tách biệt để thay heuristic packing bằng thuật toán khác sau POC. | Should |

## 8. Preliminary Story Map

### Activity 1. Chuẩn bị dữ liệu

- Chọn vị trí pallet.
- Xem thông số pallet áp dụng.
- Chọn `Carton Code`.
- Nhập số lượng từng loại box.
- Kiểm tra lỗi validate.

### Activity 2. Sinh phương án

- Chạy auto-packing.
- Nhận phương án xếp đầu tiên.
- Xem utilization và layer count.

### Activity 3. Kiểm tra trực quan

- Mở 3D workspace.
- Zoom / rotate để quan sát.
- Chọn box để xem vị trí và orientation.

### Activity 4. Điều chỉnh

- Kéo thả box.
- Xoay box.
- Xem lại trạng thái hợp lệ và metric sau chỉnh sửa.

### Activity 5. Chốt kết quả

- So sánh phương án hiện tại với mục tiêu sử dụng không gian.
- Quyết định chấp nhận phương án POC.

## 9. UI And Screen Coverage Assessment

| Screen | Coverage assessment | Backbone note |
| --- | --- | --- |
| SCR-01 Input cấu hình pallet và box | Critical | Cần thể hiện rõ pallet context, catalog box, quantity input, validation |
| SCR-02 3D packing workspace | Critical | Là màn hình khác biệt nhất của sản phẩm; cần flow và trạng thái chi tiết |
| SCR-03 Kết quả và validation | Critical | Cần trình bày metric, trạng thái hợp lệ, và hành động chỉnh tay/reset |

### UI assessment

- Phạm vi có UI-backed screens rõ ràng, đủ điều kiện mở FRD, user stories, SRS chọn lọc và wireframes.
- `SCR-02` là screen có rủi ro delivery cao nhất vì phụ thuộc đồng thời vào dữ liệu packing, 3D rendering, và interaction.

## 10. Artifact Emission Gates

| Artifact | Gate | Decision |
| --- | --- | --- |
| FRD | Có nhiều feature, workflow, business rules và cần handoff POC rõ ràng | Emit |
| User stories | Cần input cho delivery và acceptance criteria | Emit |
| SRS | Có UI screens, interaction 3D, validation logic và algorithm flow cần đặc tả chọn lọc | Emit |
| Wireframes | Có 3 screen lõi và 3D workspace cần contract rõ | Emit |
| Technical deep dive | Chỉ ở mức chọn lọc, tập trung validate/input/workspace/packing flow | Emit selective only |

## 11. Key Business Rules Draft

- BR-01: Phương án xếp không được vượt kích thước pallet theo chiều dài và chiều rộng.
- BR-02: Phương án xếp không được vượt giới hạn chiều cao theo vị trí pallet.
- BR-03: Khi chọn box từ catalog chuẩn, kích thước box phải lấy từ master data tương ứng với `Carton Code`.
- BR-04: Dữ liệu đầu vào phải hợp lệ trước khi chạy auto-packing.
- BR-05: Mọi chỉnh sửa tay phải được phản ánh vào trạng thái hợp lệ và metric kết quả.
- BR-06: `Utilization` là tiêu chí đánh giá chính của phương án gợi ý trong phạm vi POC.

## 12. Assumptions

- A-01: Luồng chính của POC dùng catalog box chuẩn, không phụ thuộc nhập kích thước tự do.
- A-02: `Annual volume`, `annual volume weight`, và `freight cost` chưa là driver chính cho thuật toán.
- A-03: Heuristic packing là chấp nhận được cho POC nếu cho ra phương án trực quan, hợp lệ, và đủ nhanh.
- A-04: Người dùng thao tác trên desktop/laptop thay vì thiết bị di động.

## 13. Risks

- R-01: Chưa có KPI định lượng cuối cùng nên khó chốt ngưỡng thành công POC.
- R-02: Chưa xác nhận rõ decision maker nghiệp vụ.
- R-03: Chưa khóa hoàn toàn việc có cho nhập box ngoài catalog chuẩn hay không.
- R-04: 3D interaction trên web có thể làm tăng độ phức tạp implementation so với POC đơn giản.
- R-05: Nếu manual drag/drop không có constraint rõ, trạng thái hợp lệ sau chỉnh sửa có thể khó kiểm soát.

## 14. Open Questions

- OQ-01: POC có cho phép thêm box ngoài catalog chuẩn hay không.
- OQ-02: `Volume weight` và `freight cost` chỉ để hiển thị tham chiếu hay sẽ tham gia báo cáo/ưu tiên.
- OQ-03: Người dùng có cần lưu hoặc export phương án xếp sau chỉnh tay không.
- OQ-04: Có cần hỗ trợ nhiều phương án gợi ý hay chỉ một phương án tốt nhất.
- OQ-05: Danh sách vị trí pallet hỗ trợ trong POC gồm chính xác những option nào trong UI.

## 15. Recommended Downstream Focus

### FRD focus

- Flow chọn pallet, chọn box catalog, nhập số lượng, chạy packing, xem kết quả, chỉnh tay.
- Quy tắc validate input và business rules của catalog box.
- Mô tả rõ 3D workspace và hành vi metric/result.

### Stories focus

- Epic quản lý context pallet và box catalog.
- Epic auto-packing và review kết quả.
- Epic 3D workspace và manual adjustment.

### SRS focus

- Use case cho `Create packing plan`, `Review 3D layout`, `Adjust layout manually`.
- Screen Contract Lite cho 3 màn hình lõi.
- Quy tắc validation và state handling sau chỉnh tay.
