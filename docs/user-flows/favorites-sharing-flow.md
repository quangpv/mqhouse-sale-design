# Luồng yêu thích và chia sẻ

## 1. Flow Overview
- **Flow name**: Luồng yêu thích và chia sẻ BĐS
- **Actor**: All logged-in users
- **Description**: Quy trình thêm/xoá BĐS yêu thích, xem lịch sử, chia sẻ thông tin BĐS

## 2. Preconditions
- BĐS hoặc phòng tồn tại
- User có quyền xem BĐS đó

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | property-detail.md | User tap icon tim (heart) → thêm yêu thích | FAV-01 |
| 2 | room-detail.md | User tap icon tim → thêm yêu thích | FAV-02 |
| 3 | search.md / map.md | User tap icon tim trên card → thêm yêu thích | FAV-01, FAV-02 |
| 4 | my-properties.md (tab) | User chuyển tab "Yêu thích" → xem danh sách | FAV-03 |
| 5 | dashboard.md | User xem "Xem gần đây" trên Dashboard | FAV-04 |
| 6 | — | [Optional] User xoá lịch sử / yêu thích | FAV-05 |
| 7 | property-detail / room-detail | User tap "Chia sẻ" → mở sharing.md | SHARE |
| 8 | sharing.md | User chọn thông tin cần chia sẻ | SHARE-01..04 |
| 9 | sharing.md | User tap Quick share (Zalo/Facebook/Copy) | SHARE-01, SHARE-02, SHARE-03 |
| 10 | sharing.md | [Optional] User tap "Chia sẻ ảnh" | SHARE-04 |

## 4. Alternate Flows
- **Bỏ yêu thích**: Tap lại icon tim → unfavorite
- **Chia sẻ native**: [ASSUMPTION] Sử dụng platform share sheet nếu không có app Zalo/Facebook
- **Chia sẻ qua Zalo/Facebook không có app**: Fallback về web URL
- **Copy link**: Toast "Đã sao chép link"

## 5. Error Handling
- **Share action thất bại**: Toast "Chia sẻ thất bại, vui lòng thử lại"
- **Không tìm thấy BĐS đã yêu thích**: [ASSUMPTION] Card bị ẩn hoặc hiển thị "BĐS không còn tồn tại"
- **Yêu thích trùng**: [ASSUMPTION] API trả về conflict → toast "BĐS đã có trong danh sách yêu thích"

## 6. Screens Involved
- property-detail.md
- room-detail.md
- my-properties.md
- dashboard.md
- search.md
- map.md
- sharing.md

## 7. Gaps
- [DESIGN GAP] FAV-04 (Lịch sử xem) — danh sách "Xem gần đây" tồn tại trên Dashboard nhưng không có màn hình riêng
- [DESIGN GAP] FAV-05 (Xoá lịch sử / yêu thích) — không có delete UI trong HTML
