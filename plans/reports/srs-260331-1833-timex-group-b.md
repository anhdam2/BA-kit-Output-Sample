# SRS Group B - Behavioral

## 1. Metadata

- Project: TimeX
- Slug: `timex`
- Date set: `260331-1833`
- Source group A: `plans/reports/srs-260331-1833-timex-group-a.md`
- Source user stories: `plans/reports/user-stories-260331-1833-timex.md`

## 2. Use Case Specifications

### UC-01 Configure Packing Request

| Field | Value |
| --- | --- |
| Goal | Chuẩn bị request hợp lệ để chạy auto-packing |
| Primary actor | Nhân viên kho |
| Supporting systems | Box catalog service, pallet configuration service |
| Linked stories | `US-01`, `US-02`, `US-03`, `US-04` |
| Linked FR | `FR-01` đến `FR-07` |
| Linked screens | `SCR-01` |
| Preconditions | Người dùng đã mở ứng dụng; dữ liệu pallet position và box catalog sẵn sàng |
| Postconditions | Request hợp lệ được giữ trên client state và có thể gửi sang auto-packing |

Main flow:

1. Người dùng mở `SCR-01`.
2. Hệ thống hiển thị danh sách vị trí pallet hỗ trợ.
3. Người dùng chọn một vị trí pallet.
4. Hệ thống nạp kích thước pallet và giới hạn chiều cao tương ứng.
5. Người dùng tìm và chọn một hoặc nhiều `Carton Code` từ catalog chuẩn.
6. Hệ thống thêm từng loại box vào danh sách đã chọn và tự nạp kích thước chuẩn.
7. Người dùng nhập số lượng cho từng loại box.
8. Người dùng yêu cầu chạy auto-packing.
9. Hệ thống validate toàn bộ request.
10. Hệ thống chuyển request hợp lệ sang use case `UC-02`.

Alternate flows:

- A1. Ở bước 3, nếu chưa chọn vị trí pallet thì bước 8 bị chặn và hệ thống hiển thị lỗi bắt buộc.
- A2. Ở bước 5, nếu không tìm thấy `Carton Code` thì hệ thống giữ nguyên danh sách đã chọn và hiển thị trạng thái không có kết quả.
- A3. Ở bước 7, nếu số lượng rỗng, không phải số nguyên, hoặc nhỏ hơn 1 thì bước 8 bị chặn và dòng lỗi xuất hiện ngay tại box item tương ứng.
- A4. Ở bước 9, nếu request thiếu box item hợp lệ thì hệ thống hiển thị banner lỗi tổng hợp và không gọi auto-packing.

### UC-02 Generate Auto-packing Plan

| Field | Value |
| --- | --- |
| Goal | Sinh layout xếp box khả thi dựa trên request hợp lệ |
| Primary actor | Nhân viên kho |
| Supporting systems | Auto-packing service |
| Linked stories | `US-05`, `US-06` |
| Linked FR | `FR-08`, `FR-09`, `FR-16` |
| Linked screens | `SCR-01`, `SCR-02`, `SCR-03` |
| Preconditions | `UC-01` đã hoàn tất với request hợp lệ |
| Postconditions | Một layout baseline được tạo cùng metric và validation state ban đầu |

Main flow:

1. Người dùng bấm `Run Auto-packing`.
2. Hệ thống gửi packing request gồm pallet context và box items sang auto-packing service.
3. Auto-packing service tính toán layout gợi ý đầu tiên.
4. Hệ thống nhận về danh sách box placements, `utilization`, `layer count`, và `validation state`.
5. Hệ thống hiển thị layout baseline tại `SCR-02`.
6. Hệ thống hiển thị metric và trạng thái tại `SCR-03`.

Alternate flows:

- B1. Nếu auto-packing không trả về layout khả thi, hệ thống hiển thị trạng thái thất bại tại `SCR-03` và không mở workspace ở chế độ thành công.
- B2. Nếu dịch vụ phản hồi quá thời gian chờ POC, hệ thống hiển thị thông báo thử lại và giữ nguyên request trước đó.
- B3. Nếu layout được tạo nhưng `validation state` là cảnh báo, hệ thống vẫn hiển thị kết quả nhưng gắn nhãn cần kiểm tra.

### UC-03 Review 3D Layout

| Field | Value |
| --- | --- |
| Goal | Kiểm tra trực quan layout đã sinh trong không gian 3D |
| Primary actor | Nhân viên kho |
| Supporting systems | 3D workspace renderer |
| Linked stories | `US-07`, `US-08` |
| Linked FR | `FR-10`, `FR-11`, `FR-12` |
| Linked screens | `SCR-02` |
| Preconditions | Có layout baseline từ `UC-02` |
| Postconditions | Người dùng hiểu vị trí và orientation của box đang kiểm tra |

Main flow:

1. Hệ thống mở `SCR-02` với pallet và box placements.
2. Người dùng dùng `zoom` để thay đổi khoảng cách camera.
3. Người dùng dùng `rotate` để xoay góc nhìn.
4. Người dùng chọn một box bất kỳ trên workspace.
5. Hệ thống highlight box được chọn và hiển thị thông tin vị trí, orientation, layer tương ứng.

Alternate flows:

- C1. Nếu chưa có layout thì `SCR-02` hiển thị empty state thay vì canvas đầy đủ.
- C2. Nếu người dùng chọn box khác, hệ thống bỏ highlight box cũ và cập nhật panel chi tiết.
- C3. Nếu renderer không tải được dữ liệu layout, hệ thống hiển thị lỗi kỹ thuật và nút quay lại kết quả.

### UC-04 Adjust Layout Manually

| Field | Value |
| --- | --- |
| Goal | Cho phép thử chỉnh tay layout và đánh giá lại tính hợp lệ |
| Primary actor | Nhân viên kho |
| Supporting systems | 3D workspace renderer, validation engine |
| Linked stories | `US-09`, `US-10`, `US-11` |
| Linked FR | `FR-13`, `FR-14`, `FR-15`, `FR-16` |
| Linked screens | `SCR-02`, `SCR-03` |
| Preconditions | Có layout baseline hoặc layout hiện hành đang mở trong workspace |
| Postconditions | Layout hiện hành được cập nhật; metric và validation state phản ánh trạng thái mới nhất |

Main flow:

1. Người dùng chọn một box trong `SCR-02`.
2. Người dùng kéo box sang vị trí mới hoặc kích hoạt thao tác xoay.
3. Hệ thống cập nhật layout tạm thời trên workspace.
4. Hệ thống gửi layout hiện hành sang validation engine.
5. Validation engine tính lại `validation state`, `utilization`, và `layer count`.
6. Hệ thống cập nhật `SCR-02` và `SCR-03` theo kết quả mới.

Alternate flows:

- D1. Nếu box bị kéo ra ngoài biên pallet hoặc vượt chiều cao, hệ thống gắn trạng thái không hợp lệ và hiển thị cảnh báo.
- D2. Nếu orientation mới gây chồng lấn box, hệ thống vẫn giữ layout hiện hành nhưng đánh dấu lỗi để người dùng tiếp tục chỉnh.
- D3. Nếu validation engine lỗi, hệ thống giữ thay đổi trực quan gần nhất nhưng khóa trạng thái `confirmed valid`.

### UC-05 Reset To Auto-pack Baseline

| Field | Value |
| --- | --- |
| Goal | Khôi phục layout baseline nhanh sau khi chỉnh tay |
| Primary actor | Nhân viên kho |
| Supporting systems | Layout state manager |
| Linked stories | `US-12` |
| Linked FR | `FR-17` |
| Linked screens | `SCR-03`, `SCR-02` |
| Preconditions | Có layout baseline và đã phát sinh manual change |
| Postconditions | Workspace và metric quay về trạng thái baseline |

Main flow:

1. Người dùng chọn `Reset to Auto-pack`.
2. Hệ thống nạp lại layout baseline.
3. Hệ thống cập nhật `SCR-02` về bố cục baseline.
4. Hệ thống cập nhật `SCR-03` với metric và trạng thái baseline.

Alternate flows:

- E1. Nếu chưa có manual change thì hành động reset ở trạng thái disabled.
- E2. Nếu baseline layout không còn tồn tại trong session thì hệ thống yêu cầu chạy auto-packing lại.

