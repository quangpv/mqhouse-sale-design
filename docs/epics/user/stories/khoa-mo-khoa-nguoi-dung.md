## USER-04: Khóa/Mở khóa người dùng

- **Tên:** Khóa/Mở khóa tài khoản
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **khóa hoặc mở khóa tài khoản người dùng**, So that **kiểm soát truy cập hệ thống**

**Priority:** High

**Acceptance Criteria:**
- [ ] Nút "Khóa" / "Mở khóa" trên mỗi user
- [ ] Confirm dialog
- [ ] Khi khóa → user không thể đăng nhập
- [ ] Khi mở khóa → user đăng nhập lại bình thường
- [ ] Không thể khóa Super Admin
- [ ] Ghi lại lịch sử khóa/mở khóa

## Technical Tasks

### Backend
- `PUT /api/users/:id/toggle-lock`
- Không khóa được Super Admin

### Frontend
- Lock/unlock button + confirm
