# Chia sẻ

## 1. Screen Overview
- **Screen name**: Chia sẻ (Sharing)
- **Purpose**: Cho phép người dùng chọn thông tin BĐS/phòng để xuất bản và chia sẻ đến khách hàng qua các nền tảng
- **Business context**: Sale cần chia sẻ thông tin nhà/phòng cho khách hàng tiềm năng qua Zalo, Facebook, hoặc sao chép link

## 2. UI Structure
### Layout sections
- **Header**: Nút back (goBack), tiêu đề "Chia sẻ"
- **Property summary card**: Ảnh thumbnail, badge type/status, tên BĐS, giá
- **Instruction text**: "Chọn các thông tin cần xuất bản và chia sẻ đến khách hàng của bạn."
- **Info sections** (6 mục, mỗi mục có checkbox toggle):
  1. Địa chỉ (Address) — địa chỉ đầy đủ
  2. Loại phòng (Room type) — hiển thị màu primary
  3. Nội thất (Furniture) — chips: bed, wardrobe, desk, sofa, kitchen cabinet
  4. Dịch vụ (Services) — chips kèm giá: electricity, water, management fee, internet
  5. Tiện ích (Amenities) — chips: pool, gym, security, fingerprint lock, BBQ area
  6. Toggle unchecked → content fade 40% opacity
- **Share actions footer**:
  - Quick share row: Zalo (#0068FF), Facebook (SVG icon), Copy link
  - Grid row: "Chia sẻ ảnh" và "Chia sẻ tin" — primary styled buttons
- **Toast**: Bottom-center, trigger bởi bất kỳ share action nào

### Components
- **Property card**: Thumbnail + badge + title + price
- **Checkbox toggle**: Mỗi info section có checkbox, unchecked làm mờ nội dung
- **Chip group**: Hiển thị các tag dạng chip cho furniture/services/amenities
- **Quick share buttons**: Zalo (blue), Facebook (icon SVG), Copy
- **Action buttons**: "Chia sẻ ảnh", "Chia sẻ tin" — full-width primary
- **Toast**: Bottom-center notification

### Important UI patterns
- Checkbox toggle kiểm soát visibility của từng section — hỗ trợ custom nội dung chia sẻ
- Fade opacity 40% khi unchecked thay vì ẩn hoàn toàn
- Chips hiển thị dạng horizontal scroll nếu overflow
- Toast xuất hiện với message tương ứng theo action

## 3. Entry Points
- **Property Detail**: Nút "Chia sẻ" trên property-detail.html
- **Room Detail**: Nút "Chia sẻ" trên room-detail.html
- **My Properties**: [ASSUMPTION] Có thể truy cập từ danh sách BĐS của user

## 4. States
- **Loading**: [ASSUMPTION] Skeleton loading cho property card khi đang load dữ liệu
- **Empty**: [ASSUMPTION] Nếu BĐS không tồn tại → redirect về màn hình trước
- **Error**: [ASSUMPTION] Toast lỗi nếu share action thất bại
- **Success**: Toast "Đã sao chép link" / "Đã chia sẻ qua Zalo" / v.v.

## 5. Business Rules
### Validation rules
- [ASSUMPTION] Cần ít nhất 1 info section được chọn mới cho phép share
- [ASSUMPTION] Dung lượng ảnh share phải < 10MB

### Permission rules
- Bất kỳ user đã đăng nhập nào cũng có thể share BĐS
- [ASSUMPTION] Cần quyền xem BĐS đó (không share BĐS của người khác nếu không có quyền)

### Conditional rendering rules
- Quick share buttons luôn hiển thị
- Info sections render động dựa trên dữ liệu BĐS (nếu không có nội thất → ẩn section)
- Service chips kèm giá, amenity chips chỉ hiển thị tên

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| SHARE-01 | Chia sẻ qua Zalo | Done |
| SHARE-02 | Chia sẻ qua Facebook | Done |
| SHARE-03 | Sao chép link | Done |
| SHARE-04 | Chia sẻ hình ảnh | Done |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Property Detail | Sharing | Tap "Chia sẻ" |
| Room Detail | Sharing | Tap "Chia sẻ" |
| Sharing | Property/Room Detail | Back button (goBack) |

## 8. Mapping Notes
- **HTML**: `mqhouse-sale-design/sharing.html` (317 lines)
- **JS behaviors**:
  - `triggerAction(message)`: gọi khi click quick share, hiển thị toast
  - `setupToggleInteraction(checkboxId, containerId)`: kiểm soát fade effect
- [STORY GAP] KHÔNG có user story cho việc custom nội dung trước khi share (info section toggle) — đây là feature mở rộng
- [ASSUMPTION] Zalo/Facebook share sử dụng deeplink hoặc URL scheme
- [ASSUMPTION] Copy link copy URL của BĐS vào clipboard
- [ASSUMPTION] "Chia sẻ ảnh" export ảnh property card + info, "Chia sẻ tin" tạo bài đăng ngắn
