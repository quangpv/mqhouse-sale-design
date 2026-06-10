# Luồng quản lý người dùng

## 1. Flow Overview
- **Flow name**: Luồng quản lý người dùng
- **Actor**: Super Admin, Admin
- **Description**: Quy trình quản lý tài khoản thành viên, phân quyền và vai trò

## 2. Preconditions
- User có quyền Admin hoặc Super Admin
- [ASSUMPTION] Các role mặc định đã được khởi tạo

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | members.md | Admin xem danh sách user | USER-01 |
| 2 | members.md | [Optional] Admin dùng search/filter tabs | USER-01 |
| 3 | members.md (dialog) | Admin tap "Thêm" → điền form → tạo user | USER-02 |
| 4 | members.md (dialog) | [Optional] Admin chọn tỉnh/huyện/xã cho user | USER-06 |
| 5 | members.md (dialog) | Admin sửa thông tin user | USER-03 |
| 6 | members.md | Admin khoá/mở khoá user | USER-04 |
| 7 | permissions.md | Admin cấu hình quyền cho role | USER-05 |
| 8 | — | [SA only] Tạo/sửa role mới | USER-07 |

## 4. Alternate Flows
- **Không thể xoá chính mình**: Disable action cho user hiện tại
- **Không thể tạo user với role cao hơn role của mình**: Validation "Bạn không có quyền tạo user với role này"
- **Username đã tồn tại**: Error "Username này đã được sử dụng"
- **[ASSUMPTION] Email/SĐT đã tồn tại**: Error "Email/Số điện thoại đã được đăng ký"

## 5. Error Handling
- **Mất kết nối khi lưu**: Toast "Lưu thất bại, vui lòng thử lại"
- **Xoá user đang hoạt động**: [ASSUMPTION] Warning "User này đang quản lý BĐS. Bạn có chắc chắn muốn xoá?"
- **[ASSUMPTION] Conflict**: Nếu có người dùng khác đang chỉnh sửa cùng lúc → "Dữ liệu đã thay đổi, vui lòng tải lại"

## 6. Screens Involved
- members.md
- permissions.md

## 7. Gaps
- [DESIGN GAP] USER-07 (Quản lý vai trò) — chỉ có permission assignment, chưa có role CRUD UI
- [STORY GAP] Phân quyền chi tiết (module-level) chưa được xác định rõ
