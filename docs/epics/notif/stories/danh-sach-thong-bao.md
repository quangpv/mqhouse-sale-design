# NOTIF-01: Danh sách thông báo

- **Role:** Tất cả người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem danh sách thông báo**, So that **không bỏ lỡ thông tin quan trọng**

**Priority:** High

**Acceptance Criteria:
- [ ] Danh sách thông báo theo thời gian (mới nhất đầu)
- [ ] Mỗi item: icon loại TB, tiêu đề, nội dung tóm tắt, thời gian
- [ ] Badge số lượng chưa đọc trên icon
- [ ] Phân trang hoặc infinite scroll
- [ ] Filter theo loại thông báo
- [ ] Click vào TB → xem chi tiết

## Technical Tasks

### Backend
- Bảng `thong_bao`
- `GET /api/notifications` - danh sách (phân trang)
- `GET /api/notifications/unread-count` - số chưa đọc

### Frontend
- Màn hình notifications.html
- Badge trên tab/bell icon
