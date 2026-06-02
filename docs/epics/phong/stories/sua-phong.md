## PHONG-03: Sửa phòng

- **Tên:** Cập nhật thông tin phòng
- **Role:** HouseHolder (của mình), Manager (trong KV), Admin, Super Admin
- **Mô tả:** As a **người quản lý**, I want **sửa thông tin phòng**, So that **thông tin phòng luôn chính xác**

**Priority:** High

**Acceptance Criteria:**
- [ ] Form sửa với dữ liệu hiện tại
- [ ] Sửa tất cả các trường: giá thuê, nội thất, dịch vụ, hình ảnh
- [ ] Khi sửa giá thuê → ghi lại lịch sử giá
- [ ] Thêm/xóa hình ảnh

## Technical Tasks

### Backend
- `PUT /api/rooms/:id` - cập nhật phòng
- `GET /api/rooms/:id/edit` - dữ liệu cho form sửa
- Kiểm tra quyền sở hữu phòng

### Frontend
- Form sửa phòng
- Pre-fill dữ liệu
