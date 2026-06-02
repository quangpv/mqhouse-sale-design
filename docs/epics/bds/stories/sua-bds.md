# BDS-03: Sửa Bất động sản

- **Role:** HouseHolder (của mình), Manager (trong KV), Admin, Super Admin
- **Mô tả:** As a **người có quyền sửa**, I want **cập nhật thông tin BĐS**, So that **thông tin luôn chính xác và cập nhật**

**Priority:** High

**Acceptance Criteria:**
- [ ] Mở form sửa với dữ liệu hiện tại
- [ ] Sửa tất cả các trường giống khi tạo
- [ ] Thêm/xóa/sắp xếp lại hình ảnh
- [ ] Nếu sửa bởi HouseHolder/Manager và BĐS đã duyệt → về "chờ duyệt"
- [ ] Nếu sửa bởi Admin/Super Admin → giữ nguyên trạng thái
- [ ] Lưu lịch sử chỉnh sửa

## Technical Tasks

### Backend
- UPDATE bảng `bat_dong_san` + xóa/thêm bảng con (hình ảnh, nội thất, tiện ích)
- `PUT /api/properties/:id` - cập nhật BĐS
- `GET /api/properties/:id/edit` - lấy dữ liệu cho form sửa
- Kiểm tra quyền sửa: chủ sở hữu hoặc Admin

### Frontend
- Form sửa (dùng lại component tạo)
- Pre-fill dữ liệu hiện tại
