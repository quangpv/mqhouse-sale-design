## USER-02: Tạo người dùng

- **Tên:** Thêm người dùng mới
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **tạo tài khoản người dùng mới**, So that **cấp quyền truy cập hệ thống**

**Priority:** High

**Acceptance Criteria:**
- [ ] Dialog form tạo user: tên đăng nhập, mật khẩu, họ tên, email, SĐT
- [ ] Chọn vai trò (dropdown)
- [ ] Chọn khu vực quản lý (tỉnh/quận/phường) - nếu là Manager
- [ ] Upload avatar
- [ ] Validate các trường
- [ ] Tạo thành công → tự động gửi thông báo/xác nhận

## Technical Tasks

### Backend
- `POST /api/users` - tạo user
- `POST /api/users/:id/areas` - gán khu vực
- Chỉ Admin/Super Admin

### Frontend
- Dialog tạo user (members.html)
- Cascading dropdown địa giới HC
- Avatar upload
- Validate trùng tên đăng nhập
