# NOTIF-02: Xem chi tiết thông báo

- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem chi tiết thông báo**, So that **nắm được nội dung đầy đủ**

**Priority:** Medium

**Acceptance Criteria:
- [ ] Hiển thị: tiêu đề, nội dung đầy đủ, thời gian
- [ ] Hiển thị loại thông báo
- [ ] Nếu có entity (BDS/Phòng) → link đến chi tiết entity
- [ ] Tự động đánh dấu đã đọc khi xem

## Technical Tasks

### Backend
- `GET /api/notifications/:id`

### Frontend
- Notification detail screen
- Deep link đến entity
