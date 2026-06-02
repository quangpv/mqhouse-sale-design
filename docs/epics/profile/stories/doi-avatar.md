# PROFILE-03: Đổi avatar

- **Tên:** Đổi ảnh đại diện
- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **đổi ảnh đại diện**, So that **cá nhân hóa tài khoản**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Click vào avatar → mở dialog upload
- [ ] Upload từ thư viện hoặc chụp ảnh
- [ ] Crop/Resize ảnh
- [ ] Xem trước trước khi lưu
- [ ] Lưu → cập nhật avatar ngay

## Technical Tasks

### Backend
- `PUT /api/profile/avatar` - upload avatar

### Frontend
- Avatar upload component (crop, preview)
