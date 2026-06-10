# Luồng thông báo

## 1. Flow Overview
- **Flow name**: Luồng thông báo
- **Actor**: All logged-in users
- **Description**: Quy trình xem, đánh dấu đã đọc và quản lý thông báo

## 2. Preconditions
- User đã đăng nhập
- [ASSUMPTION] Hệ thống đã tạo thông báo (thủ công hoặc tự động)

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | notifications.md | User xem danh sách thông báo | NOTIF-01 |
| 2 | notifications.md | User tap "Đánh dấu đã đọc" → tất cả chuyển read | NOTIF-03 |
| 3 | — | [Optional] User tap vào thông báo → xem chi tiết | NOTIF-02 [DESIGN GAP] |
| 4 | — | [Admin] Admin tạo thông báo hệ thống | NOTIF-04 [DESIGN GAP] |
| 5 | — | Hệ thống tự động gửi thông báo (duyệt/từ chối BĐS) | NOTIF-05 (backend) |
| 6 | — | [Optional] User xoá thông báo | NOTIF-06 [DESIGN GAP] |

## 4. Alternate Flows
- **Không có thông báo**: [DESIGN GAP] HTML không hiển thị empty state
- **Red dot indicator**: Tab bar hiển thị badge đỏ khi có unread (theo index.html)
- **WebSocket realtime**: [ASSUMPTION] Thông báo mới xuất hiện realtime qua WebSocket

## 5. Error Handling
- **Đánh dấu đã đọc thất bại**: Toast "Không thể cập nhật trạng thái", giữ nguyên trạng thái cũ
- **[ASSUMPTION] Quá nhiều thông báo**: Pagination hoặc infinite scroll
- **[ASSUMPTION] Kết nối realtime mất**: Fallback về polling mỗi 30s

## 6. Screens Involved
- notifications.md
- dashboard.md (tab bar badge indicator)

## 7. Gaps
- [DESIGN GAP] NOTIF-02 (Xem chi tiết thông báo) — HTML chỉ hiển thị list item, không có detail screen
- [DESIGN GAP] NOTIF-04 (Tạo thông báo hệ thống) — không có create UI
- [DESIGN GAP] NOTIF-06 (Xoá thông báo) — không có delete UI, chỉ có "Đánh dấu đã đọc"
- [STORY GAP] Empty state cho notification list — chưa được xác định
