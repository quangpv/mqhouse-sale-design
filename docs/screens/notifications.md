# Thông báo

## 1. Screen Overview
- **Screen name**: Thông báo (Notifications)
- **Purpose**: Hiển thị danh sách thông báo cho người dùng; cho phép đánh dấu đã đọc
- **Business context**: Người dùng cần theo dõi các thông báo về giảm giá, xác thực, phê duyệt BĐS và các sự kiện hệ thống khác

## 2. UI Structure
### Layout sections
- **Header**: Tiêu đề "Thông báo mới", action link "Đánh dấu đã đọc"
- **Notification list**: Danh sách các thông báo dạng vertical list
- **Tab bar**: Bottom tab bar (item "Thông báo" được highlight)

### Components
- **Notification item**: Icon circle (có màu theo loại), title, body text, timestamp
- **Unread badge** (blue background): "Giảm giá phòng!" — màu xanh dương
- **Read item** (white background): "Xác thực thành công" — màu trắng
- **Action link**: "Đánh dấu đã đọc" ở header

### Important UI patterns
- Unread = blue background, read = white background
- Timestamp hiển thị relative time ("5 phút trước", "2 giờ trước")
- Icon circle với màu sắc phân biệt theo loại thông báo (sale, system, v.v.)

## 3. Entry Points
- **Bottom tab bar**: tab "Thông báo" — luôn hiển thị ở các màn hình có tab bar
- [DESIGN GAP] Tab bar hiển thị red dot indicator khi có thông báo chưa đọc (theo index.html)

## 4. States
- **Loading**: [ASSUMPTION] Có skeleton loading khi đang tải danh sách
- **Empty**: [DESIGN GAP] Không có empty state trong HTML — cần bổ sung màn hình "Không có thông báo"
- **Error**: [DESIGN GAP] Không có error state trong HTML
- **Success**: Danh sách thông báo hiển thị với phân biệt read/unread
- **Mark all read success**: [ASSUMPTION] Toast "Đã đánh dấu tất cả là đã đọc"

## 5. Business Rules
### Validation rules
- [ASSUMPTION] Chỉ hiển thị thông báo thuộc phạm vi quyền của user

### Permission rules
- **Admin/SA**: Nhận thông báo phê duyệt BĐS, thay đổi trạng thái phòng
- **Sale**: Nhận thông báo kết quả phê duyệt yêu cầu
- **All users**: Nhận thông báo hệ thống, khuyến mãi

### Conditional rendering rules
- Nút "Đánh dấu đã đọc" chỉ hiển thị khi có thông báo chưa đọc
- Red dot trên tab bar chỉ hiển thị khi có unread notification

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| NOTIF-01 | Danh sách thông báo | Done |
| NOTIF-02 | Xem chi tiết thông báo | [DESIGN GAP] No detail screen |
| NOTIF-03 | Đánh dấu đã đọc | Done |
| NOTIF-04 | Tạo thông báo hệ thống | [DESIGN GAP] No create UI |
| NOTIF-05 | Tự động gửi thông báo | Backend behavior |
| NOTIF-06 | Xoá thông báo | [DESIGN GAP] No delete UI |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Notifications | Notification Detail | Tap notification item → [DESIGN GAP] |
| Notifications | (none) | Tap "Đánh dấu đã đọc" — inline action |
| Tab bar | Notifications | Tap "Thông báo" tab |

## 8. Mapping Notes
- **HTML**: `mqhouse-sale-design/notifications.html` (78 lines)
- **Static display only**: 2 mẫu thông báo, không có onclick handlers
- **Mẫu**: Sale notification ("Giảm giá phòng!" — blue bg) + Success notification ("Xác thực thành công" — white bg)
- [ASSUMPTION] API response format bao gồm: id, type, title, body, isRead, createdAt
- [ASSUMPTION] NOTIF-05 (auto-notify) hoàn toàn là backend behavior, không có UI tương ứng
