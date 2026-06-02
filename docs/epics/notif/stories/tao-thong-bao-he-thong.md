# NOTIF-04: Tạo thông báo hệ thống

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **tạo thông báo hệ thống gửi đến người dùng**, So that **thông báo tin tức, cập nhật**

**Priority:** Medium

**Acceptance Criteria:
- [ ] Form tạo: loại (cập nhật hệ thống, tin tức, giảm giá phòng)
- [ ] Tiêu đề, nội dung
- [ ] Chọn người nhận: tất cả / theo vai trò / theo user cụ thể
- [ ] Gửi ngay hoặc hẹn giờ
- [ ] Xem trước thông báo

## Technical Tasks

### Backend
- `POST /api/notifications/system` - tạo TB hệ thống
- `POST /api/notifications/schedule` - hẹn giờ
- Admin, Super Admin

### Frontend
- Form tạo thông báo (notifications.html - admin)
- User/role picker
