# PROFILE-02: Sửa hồ sơ

- **Tên:** Cập nhật hồ sơ
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **sửa thông tin hồ sơ của tôi**, So that **thông tin luôn cập nhật**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Form sửa: họ tên, email, số điện thoại
- [ ] Không cho sửa tên đăng nhập
- [ ] Validate các trường
- [ ] Lưu thành công → cập nhật giao diện

## Technical Tasks

### Backend
- `PUT /api/profile` - cập nhật hồ sơ

### Frontend
- Form sửa hồ sơ (user-info.html)
- Validate email, SĐT
