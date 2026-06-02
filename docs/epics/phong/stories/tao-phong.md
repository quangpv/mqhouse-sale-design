## PHONG-01: Tạo phòng

- **Tên:** Thêm phòng mới
- **Role:** HouseHolder, Manager, Admin, Super Admin
- **Mô tả:** As a **người quản lý BĐS**, I want **thêm phòng mới vào BĐS**, So that **cập nhật thông tin cho thuê chi tiết**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form tạo phòng trong tab "Thông tin phòng" của add-property
- [ ] Các trường: tên phòng, mô tả, loại phòng, diện tích, giá thuê, giá cọc
- [ ] Chọn nội thất, tiện ích cho phòng
- [ ] Chọn dịch vụ kèm theo (giá, đơn vị, chu kỳ, chỉ số đầu)
- [ ] Upload tối đa 10 hình ảnh
- [ ] Validate các trường bắt buộc
- [ ] Có thể thêm nhiều phòng cùng lúc
- [ ] Mỗi phòng có thể xóa tạm thời (trong form) trước khi lưu

## Technical Tasks

### Backend
- INSERT vào bảng `phong` + bảng liên quan (dịch vụ, nội thất, tiện ích)
- `POST /api/properties/:propertyId/rooms` - tạo phòng
- `GET /api/catalog/room-types` - loại phòng
- `GET /api/catalog/services` - dịch vụ

### Frontend
- Room form trong add-property.html
- Service dialog: chọn dịch vụ với price/unit/cycle/type/initialIndex
- Image upload cho từng phòng
- Add/remove room động
- Validate giá thuê > 0, diện tích > 0
