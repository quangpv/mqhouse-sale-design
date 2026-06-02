# NOTIF-03: Đánh dấu đã đọc

- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **đánh dấu thông báo đã đọc hoặc đánh dấu tất cả**, So that **quản lý thông báo hiệu quả**

**Priority:** Medium

**Acceptance Criteria:
- [ ] Đánh dấu 1 TB là đã đọc
- [ ] Đánh dấu tất cả là đã đọc
- [ ] Swipe để mark read (mobile)
- [ ] Badge cập nhật ngay

## Technical Tasks

### Backend
- `PUT /api/notifications/:id/read`
- `PUT /api/notifications/read-all`

### Frontend
- Swipe action, button "Đánh dấu tất cả"
