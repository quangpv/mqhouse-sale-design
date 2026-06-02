# NOTIF-06: Xóa thông báo

- **Role:** Người nhận, Admin
- **Mô tả:** As a **người dùng**, I want **xóa thông báo không cần thiết**, So that **giữ danh sách thông báo gọn gàng**

**Priority:** Low

**Acceptance Criteria:
- [ ] Xóa 1 thông báo (swipe hoặc menu)
- [ ] Xóa nhiều cùng lúc
- [ ] Xóa tất cả

## Technical Tasks

### Backend
- `DELETE /api/notifications/:id`
- `DELETE /api/notifications/bulk`

### Frontend
- Delete action, bulk select
