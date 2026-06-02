## USER-03: Sửa người dùng

- **Tên:** Cập nhật thông tin người dùng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **sửa thông tin người dùng**, So that **thông tin luôn chính xác**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Dialog sửa với dữ liệu hiện tại
- [ ] Sửa: họ tên, email, SĐT, vai trò, khu vực
- [ ] Đổi avatar
- [ ] Không cho sửa tên đăng nhập
- [ ] Admin không thể sửa thông tin Super Admin

## Technical Tasks

### Backend
- `PUT /api/users/:id`
- `PUT /api/users/:id/areas` - cập nhật khu vực
- Không cho sửa user có role cao hơn

### Frontend
- Dialog sửa (dùng chung component với tạo)
