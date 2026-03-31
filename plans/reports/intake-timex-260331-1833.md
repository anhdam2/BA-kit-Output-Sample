# Intake Form

## 1. Thông tin chung

- Tên dự án: TimeX
- Slug: `timex`
- Ngày intake: 2026-03-31 18:33 ICT
- Requester: Người dùng hiện tại
- Ngôn ngữ đầu ra mặc định: Tiếng Việt
- Engagement mode mặc định: `hybrid`
- Giai đoạn: POC
- Kênh triển khai dự kiến: Web app đơn giản nhất có thể

## 2. Bối cảnh nghiệp vụ

TimeX là hệ thống đề xuất cách sắp xếp nhiều hộp sản phẩm vào trong pallet bằng hình ảnh trực quan 3D. Nhu cầu xuất phát từ bài toán thao tác xếp hàng thủ công của nhân viên kho, nơi việc ước lượng phương án xếp còn chậm, khó hình dung không gian, và dễ phát sinh sai sót vận hành.

Hệ thống POC cần giúp nhân viên kho nhập dữ liệu hộp, xem trước cách sắp xếp trong không gian pallet, nhận đề xuất auto-packing nhằm tận dụng thể tích pallet tốt hơn, và có thể chỉnh tay lại kết quả trước khi áp dụng.

Ngoài yêu cầu nhập liệu cơ bản, phạm vi intake được bổ sung thêm một danh mục box cố định theo carton code và kích thước chuẩn từ dữ liệu nghiệp vụ cung cấp qua ảnh. Điều này cho thấy ít nhất ở POC, bài toán không chỉ là nhập kích thước tự do mà còn cần hỗ trợ chọn box từ master data cố định.

## 3. Mục tiêu và KPI sơ bộ

### Mục tiêu nghiệp vụ

- Tăng tỷ lệ sử dụng thể tích pallet.
- Giảm thời gian lên phương án xếp hàng.
- Giảm lỗi vận hành khi xếp hàng thủ công.

### KPI sơ bộ cho POC

- Hiển thị được ít nhất một phương án xếp hợp lệ từ dữ liệu đầu vào nhiều loại hộp.
- Cho phép người dùng đánh giá trực quan mức sử dụng pallet qua metric thể tích.
- Giảm thao tác thử-sai thủ công bằng cách sinh đề xuất ban đầu tự động.

### KPI còn thiếu cần xác nhận ở giai đoạn backbone

- Mức tăng mục tiêu cụ thể cho `% utilization`.
- Thời gian mục tiêu để sinh hoặc chỉnh sửa một phương án xếp.
- Ngưỡng sai sót vận hành cần giảm theo tỷ lệ hoặc số trường hợp.

## 4. Stakeholders

| Stakeholder | Vai trò | Mức ảnh hưởng | Ghi chú |
| --- | --- | --- | --- |
| Nhân viên kho | Người dùng chính | Cao | Nhập dữ liệu, xem 3D, chỉnh tay phương án |
| Lead kho / vận hành | Người phê duyệt nghiệp vụ | Trung bình | Chưa nêu rõ, cần xác nhận ở bước sau |
| Nhóm phát triển POC | Thực thi giải pháp | Trung bình | Xây web app và thuật toán POC |

## 5. Phạm vi in-scope

### 5.1 User Input

- Cho phép nhập thông tin hộp gồm:
  - chiều dài
  - chiều rộng
  - chiều cao
- Hỗ trợ nhiều loại hộp trong cùng một lần tính toán.
- Có validate dữ liệu đầu vào để tránh sai sót nhập liệu.
- Dự kiến cần hỗ trợ số lượng theo từng loại hộp để phục vụ auto-packing.
- Cần hỗ trợ ít nhất một trong hai cơ chế input:
  - nhập tay kích thước box
  - chọn box từ danh mục kích cỡ cố định theo `Carton Code`
- Với box lấy từ danh mục cố định, hệ thống nên tự nạp các thông số chuẩn và hạn chế sửa tay để tránh sai lệch dữ liệu nguồn.

### 5.1.1 Danh mục box cố định từ dữ liệu nghiệp vụ

Nguồn bổ sung từ ảnh cho thấy có tập box chuẩn với kích thước cố định, volume weight, annual volume và freight cost. Đây là dữ liệu tham chiếu quan trọng cho POC và cần được mô hình hóa như master data box.

| Description | Carton Code | Length (cm) | Width (cm) | Height (cm) | Volume Weight (kg) | Annual Volume | Annual Volume Weight (kg) | Freight Cost (USD) |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| 2 PACK POD SELF LOCKING | C02P | 14.2 | 8.9 | 11 | 0.28 | 11,100.00 | 3,086.1996 | 24,689.60 |
| 4 PACK POD SELF LOCKING | C04P | 17.3 | 14.2 | 11 | 0.54 | 2,950.00 | 1,594.3334 | 12,754.67 |
| 6 PACK POD SELF LOCKING | C06P | 22.8 | 16.4 | 11 | 0.82 | 5,110.00 | 4,203.60864 | 33,628.87 |
| 10 PACK POD SELF LOCKING | C10P | 34.5 | 16.4 | 11 | 1.24 | 20,225.00 | 25,175.271 | 201,402.17 |
| 15 PACK POD SELF LOCKING | C15P | 36.3 | 23.9 | 11 | 1.91 | 56,430.00 | 107,705.345 | 861,642.76 |
| 25 PACK POD RSC | C25R | 38.9 | 33.4 | 11 | 2.86 | 11,947.00 | 34,148.9703 | 273,191.76 |
| 50 PACK POD RSC | C50R | 38.9 | 33.4 | 19.3 | 5.02 | 44,955.00 | 225,455.781 | 1,803,646.24 |
| 40 PACK POD RSC | C40R | 38.9 | 27.0 | 19.3 | 4.05 | 7,905.00 | 32,048.119 | 256,384.95 |

Tổng cộng trong ảnh:

- Annual Volume Weight: `433,417.63 kg`
- Freight Cost: `3,467,341.02 USD`

### 5.2 Pallet Definition

- Pallet nền cố định theo vị trí đặt pallet.
- Kích thước đáy pallet: `38.9 cm x 34 cm`
- Kích thước cao cơ sở đã cung cấp: `19.3 cm`
- Thể tích tham chiếu: `25.5 lít`
- Trọng lượng tham chiếu: `1503.84 g`
- Chiều cao tối đa theo vị trí trên máy bay:
  - Lower Deck: `163 cm`
  - Main Deck: `244 cm`
  - Main Deck Freighter: `300 cm`
- Hệ thống cần phản ánh giới hạn chiều cao theo vị trí pallet khi tính phương án xếp.

### 5.3 3D Visualization

- Hiển thị mô hình 3D trực quan các hộp bên trong pallet dựa trên input.
- Hỗ trợ:
  - zoom
  - rotate
  - tương tác với box
- Mức tương tác tối thiểu cho POC:
  - chọn box
  - quan sát vị trí box
  - chỉnh sửa thủ công bằng kéo thả
  - xoay box

### 5.4 Auto-packing Algorithm

- Tự động tính toán và đề xuất cách sắp xếp hộp trong pallet.
- Ưu tiên tối đa khả năng sử dụng không gian pallet.
- Đầu ra cần đủ tốt để làm phương án khởi tạo cho thao tác chỉnh tay của người dùng.
- Cần hoạt động được với các box từ catalog cố định và các số đo chuẩn tương ứng.

### 5.5 Arrangement Output And Validation

- Hiển thị kết quả 3D sau khi sắp xếp.
- Hiển thị các metric tối thiểu:
  - tỷ lệ sử dụng không gian
  - số layer
- Cho phép người dùng kiểm soát và chỉnh sửa lại phương án bằng tay.

## 6. Phạm vi out-of-scope cho POC

- Tích hợp WMS/ERP hoặc hệ thống kho hiện hữu.
- Tối ưu theo nhiều mục tiêu nâng cao như cân bằng tải, trọng tâm, hay ràng buộc vận chuyển đặc thù.
- Quản trị người dùng, phân quyền, audit log.
- Đồng bộ dữ liệu thời gian thực với thiết bị hiện trường.
- Các ràng buộc nghiệp vụ đặc biệt như hàng dễ vỡ, không được lật, ưu tiên xếp nặng ở dưới.

## 7. Quy trình nghiệp vụ dự kiến

1. Nhân viên kho chọn vị trí pallet áp dụng.
2. Hệ thống nạp thông số pallet cố định tương ứng với vị trí đó.
3. Nhân viên kho chọn loại hộp từ danh mục carton code cố định hoặc nhập tay box nếu phạm vi POC vẫn cho phép.
4. Người dùng nhập số lượng theo từng loại hộp.
5. Hệ thống validate dữ liệu đầu vào và nạp kích thước chuẩn tương ứng với carton code.
6. Người dùng chạy auto-packing.
7. Hệ thống sinh phương án xếp và hiển thị mô hình 3D.
8. Người dùng kiểm tra metric, layer, và chỉnh sửa thủ công nếu cần.
9. Hệ thống cập nhật lại trạng thái sắp xếp sau khi chỉnh tay.

## 8. Màn hình hoặc UI được nhắc tới

| Mã sơ bộ | Màn hình | Mục đích |
| --- | --- | --- |
| SCR-01 | Input cấu hình pallet và box | Chọn carton code, nhập số lượng, validate |
| SCR-02 | 3D packing workspace | Xem mô hình 3D, rotate, zoom, chọn box |
| SCR-03 | Kết quả và validation | Xem utilization, layers, trạng thái đề xuất |

## 9. Yêu cầu thô được trích xuất

- Hệ thống đề xuất bằng hình ảnh cách sắp xếp các hộp sản phẩm vào trong pallet.
- Có phần User Input cho phép nhập thông tin box gồm độ cao, độ dài, độ rộng.
- Hỗ trợ nhiều loại hộp.
- Có data validate để tránh sai sót.
- Có 3D Visualization hiển thị box trong pallet và cho phép zoom, xoay, tương tác.
- Có auto-packing algorithm để tự động đề xuất cách sắp xếp nhằm tối đa sử dụng không gian pallet.
- Có arrangement output và validation hiển thị kết quả 3D cùng các metric như utilization, layers.
- Cho phép người dùng kiểm soát và chỉnh sửa manual bằng kéo thả, xoay box.
- Có dữ liệu box chuẩn cố định theo `Carton Code` như ảnh tham chiếu, bao gồm kích thước và dữ liệu logistic liên quan.

## 10. Ràng buộc, giả định và phụ thuộc

### Ràng buộc đã biết

- Phạm vi POC ưu tiên web app đơn giản.
- Pallet không được người dùng định nghĩa tự do mà lấy theo vị trí đặt pallet.
- Có một danh mục box chuẩn với kích thước cố định; hệ thống không nên để sai lệch master data nếu chọn theo carton code.

### Giả định làm việc

- Người dùng sẽ chọn một vị trí pallet cụ thể để hệ thống áp đúng giới hạn chiều cao.
- Dữ liệu box chuẩn có thể được seed sẵn vào hệ thống từ danh mục carton code.
- Trọng lượng/volume weight hiện là dữ liệu tham chiếu; POC chưa bắt buộc tối ưu packing theo tải trọng.
- POC chấp nhận heuristic packing thay vì tối ưu tuyệt đối miễn đầu ra trực quan và dùng được.

### Phụ thuộc

- Cần thống nhất danh sách vị trí pallet hỗ trợ trong POC.
- Cần thống nhất cơ chế lưu và quản trị danh mục box chuẩn.
- Cần lựa chọn thư viện 3D phù hợp cho web app.
- Cần xác định cách biểu diễn và cập nhật layout sau thao tác kéo thả, xoay box.

## 11. Gap analysis

| Hạng mục | Trạng thái | Nhận xét |
| --- | --- | --- |
| Stakeholders và decision maker | Thiếu một phần | Đã có người dùng chính, chưa xác nhận người duyệt nghiệp vụ |
| Problem statement | Đủ | Đã rõ bài toán tối ưu xếp hộp và trực quan hóa |
| Mục tiêu đo lường | Thiếu một phần | Có mục tiêu định tính, chưa có target số |
| In-scope / out-of-scope | Đủ ở mức POC | Đã xác định POC đơn giản |
| Compliance / regulatory | Tạm đủ | Chưa có yêu cầu tuân thủ cụ thể |
| Mô tả UI để wireframe | Đủ cho bước backbone | Có 3 vùng chức năng chính |
| Quy trình nghiệp vụ | Đủ sơ bộ | Cần chi tiết hơn ở bước stories/SRS |
| Quy tắc nghiệp vụ | Đủ hơn trước | Đã có catalog box cố định, nhưng chưa rõ có cho nhập box ngoài catalog hay không |

## 12. Câu hỏi làm rõ đã khóa scope

| Câu hỏi | Trả lời |
| --- | --- |
| Tên dự án là gì? | TimeX |
| Người dùng chính là ai? | Nhân viên kho |
| Pallet có cố định hay nhập tay? | Cố định theo vị trí đặt pallet |
| Kích thước và giới hạn pallet là gì? | Đã cung cấp base dimensions, thể tích, trọng lượng và chiều cao tối đa theo vị trí |
| Box có kích thước tự do hay cố định? | Có thêm danh mục box cố định theo carton code từ ảnh nghiệp vụ |
| Mục tiêu chính là gì? | Tăng utilization, giảm thời gian lên phương án, giảm lỗi vận hành |
| Chỉnh sửa manual đến mức nào? | Kéo thả và xoay box |
| Có ràng buộc nghiệp vụ đặc thù không? | Không có trong POC |
| Nền tảng triển khai? | Web app đơn giản |

## 13. Open questions còn lại cho downstream

- POC có cho phép nhập box ngoài danh mục carton code cố định hay chỉ được chọn từ catalog chuẩn.
- POC có cần nhập số lượng theo từng loại hộp hay chỉ một instance mỗi loại.
- Người dùng chọn vị trí pallet bằng dropdown cố định hay hệ thống tự suy ra theo ngữ cảnh.
- Có cần lưu hoặc export phương án xếp sau khi chỉnh tay không.
- Có cần so sánh nhiều phương án packing hay chỉ hiển thị một phương án tốt nhất.
- Annual volume, volume weight và freight cost có chỉ là dữ liệu tham chiếu hay sẽ tham gia vào ưu tiên packing / báo cáo.

## 14. Đề xuất scope lock

Scope POC được khóa theo hướng:

- Một web app đơn giản cho nhân viên kho.
- Input nhiều loại hộp với validate, ưu tiên chọn từ catalog box cố định theo carton code.
- Pallet cấu hình sẵn theo vị trí với giới hạn chiều cao khác nhau.
- Sinh một phương án auto-packing ưu tiên utilization.
- Hiển thị mô hình 3D có zoom, rotate, chọn box.
- Cho phép chỉnh tay bằng kéo thả và xoay box.
- Hiển thị các metric lõi như utilization và layer count.

Các nhu cầu tối ưu nâng cao, tích hợp hệ thống, và ràng buộc xếp hàng chuyên sâu được để ngoài phạm vi POC hiện tại.
