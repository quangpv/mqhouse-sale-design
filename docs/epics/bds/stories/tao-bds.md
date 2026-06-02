# BDS-01: Tạo Bất động sản

- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người có quyền tạo BĐS**, I want **nhập đầy đủ thông tin BĐS bao gồm hình ảnh, nội thất, tiện ích**, So that **đăng tin cho thuê BĐS**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form tạo BĐS dạng single scroll page với các section:
  - **Thông tin cơ bản:** mã BĐS, loại BĐS
  - **Hình ảnh:** upload tối đa 10 ảnh (grid preview, xóa từng ảnh)
  - **Vị trí địa lý:** Tỉnh/thành, Quận/huyện, địa chỉ đường, GPS auto-fill
  - **Nội thất tổng thể:** nhóm nội thất (group-item UI, thêm/sửa/xóa nhóm và item)
  - **Tiện ích tòa nhà:** nhóm tiện ích (group-item UI, thêm/sửa/xóa nhóm và item)
  - **Dịch vụ áp dụng:** grid dịch vụ với giá/đơn vị/chu kỳ/loại (cố định/theo mức sử dụng)/chỉ số đầu
  - **Thông tin mô tả:** tiêu đề bài đăng, nội dung chi tiết
  - **Thông tin liên hệ:** vai trò, Zalo link, tên liên hệ, SĐT, ghi chú hành chính
  - **Sơ đồ phòng:** grid 4 cột hiển thị phòng, click vào phòng để sửa nhanh
- [ ] Màn hình riêng "Thêm phòng mới" với các section kế thừa dữ liệu từ BDS
- [ ] Nút "Thêm phòng" để chuyển sang màn hình tạo phòng
- [ ] Có thể thêm nhiều mã phòng cùng lúc (batch input)
- [ ] Validate các trường bắt buộc
- [ ] Tự động lưu nháp (draft) nếu chưa hoàn thành
- [ ] Nút "Xác nhận tạo" ở footer sticky
- [ ] Khi tạo bởi HouseHolder/Manager → trạng thái "chờ duyệt"
- [ ] Khi tạo bởi Admin/Super Admin → trạng thái "đã duyệt"

## Technical Tasks

### Backend
- INSERT vào bảng `bat_dong_san` + bảng liên quan (hình ảnh, nội thất, tiện ích, dịch vụ)
- `POST /api/properties` - tạo BĐS mới (multipart/form-data nếu có file)
- `POST /api/upload` - upload hình ảnh (tối đa 10)
- `DELETE /api/upload/:id` - xóa hình ảnh
- `GET /api/catalog/furniture` - danh sách nội thất để chọn
- `GET /api/catalog/utilities` - danh sách tiện ích để chọn
- `GET /api/catalog/property-types` - loại BĐS
- `GET /api/catalog/services` - danh sách dịch vụ
- GPS auto-fill: nhận tọa độ → tra ngược địa chỉ (Reverse Geocoding)
- HouseHolder/Manager → trạng thái "chờ duyệt"
- Admin/Super Admin → trạng thái "đã duyệt"

### Frontend
- Màn hình add-property.html: single scroll page với các section
- Màn hình thêm phòng riêng: screen-them-phong với kế thừa dữ liệu BDS
- Image upload với preview, xóa từng ảnh
- Group-item UI cho nội thất/tiện ích (thêm/sửa/xóa nhóm và item)
- Service dialog: type toggle (cố định/theo mức sử dụng), price, unit, cycle, initial index
- Sơ đồ phòng grid: 4 cột, click để sửa nhanh (quick-update bottom sheet)
- Batch room code input (thêm/xóa nhiều mã phòng cùng lúc)
- GPS auto-fill location button
- Validation form
- Validate mã BĐS không để trống
- Validate diện tích > 0, giá thuê > 0
- Tối đa 10 hình ảnh, định dạng: jpg, png, webp
