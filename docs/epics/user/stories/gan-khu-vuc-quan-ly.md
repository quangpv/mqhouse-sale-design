## USER-06: Gán khu vực quản lý

- **Tên:** Gán khu vực quản lý cho người dùng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **gán tỉnh/quận/huyện/phường cho Manager**, So that **họ chỉ quản lý BĐS trong khu vực được giao**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Trong form tạo/sửa user, phần "Khu vực quản lý"
- [ ] Cascading dropdown: Chọn Tỉnh → Quận/Huyện → Phường/Xã
- [ ] Có thể chọn nhiều khu vực
- [ ] Hiển thị danh sách khu vực đã chọn (dạng tag/chip)
- [ ] Xóa khu vực khỏi danh sách
- [ ] Manager khi đăng nhập chỉ thấy BĐS trong KV được gán

## Technical Tasks

### Backend
- Bảng `user_area`: user_id + area_id
- `POST /api/users/:id/areas` - gán khu vực
- `DELETE /api/users/:id/areas/:areaId` - xóa
- `GET /api/locations` - danh sách địa giới HC

### Frontend
- Cascading dropdown component
- Tag/chip hiển thị khu vực đã chọn
