# Luồng hồ sơ và tài khoản

## 1. Flow Overview
- **Flow name**: Luồng hồ sơ và tài khoản người dùng
- **Actor**: All logged-in users
- **Description**: Quy trình xem và chỉnh sửa thông tin cá nhân, đổi mật khẩu, đăng xuất

## 2. Preconditions
- User đã đăng nhập

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | profile.md | User xem trang hồ sơ cá nhân | PROFILE-01 |
| 2 | user-info.md | User xem/sửa thông tin cá nhân | PROFILE-02 |
| 3 | profile.md | User tap icon camera → đổi avatar | PROFILE-03 |
| 4 | profile.md / user-info.md | User xem thông tin tài khoản (role, mã số) | PROFILE-04 |
| 5 | change-password.md | User tap "Đổi mật khẩu" → cập nhật | AUTH-06 |
| 6 | — | User tap "Đăng xuất" → quay về màn hình Login | — |
| 7 | my-properties.md | [Optional] User xem danh sách BĐS của mình | BDS-08 |
| 8 | my-properties.md (tab) | [Optional] User xem danh sách yêu thích | FAV-03 |

## 4. Alternate Flows
- **Xem trang tĩnh**: [DESIGN GAP] Giới thiệu, Liên hệ/Hỗ trợ, Điều khoản — chưa có UI
- **Fullscreen toggle**: [ASSUMPTION] postMessage to parent (webview) — hỗ trợ chế độ fullscreen
- **[ASSUMPTION] Đổi avatar**: Camera → crop → upload → preview

## 5. Error Handling
- **Upload avatar thất bại**: Toast "Tải ảnh lên thất bại", giữ avatar cũ
- **Lưu thông tin thất bại**: Toast "Cập nhật thất bại, vui lòng thử lại"
- **Mật khẩu cũ không đúng** (change-password): Error "Mật khẩu hiện tại không chính xác"

## 6. Screens Involved
- profile.md
- user-info.md
- change-password.md
- my-properties.md
