# Luồng quản lý danh mục

## 1. Flow Overview
- **Flow name**: Luồng quản lý danh mục hệ thống
- **Actor**: Super Admin, Admin (R for others)
- **Description**: Quy trình quản lý địa giới hành chính, loại BĐS/phòng, nội thất, tiện ích, dịch vụ

## 2. Preconditions
- User có quyền quản lý danh mục (Admin/SA)
- [ASSUMPTION] Dữ liệu seed mặc định đã được khởi tạo

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | catalog.md | Admin mở trang quản lý danh mục | CAT |
| 2 | catalog.md (Tab 1) | Admin chọn tab Địa giới hành chính | CAT-01 |
| 3 | catalog.md (bottom sheet) | [Optional] Admin thêm Tỉnh/Thành phố | CAT-01 |
| 4 | catalog.md (tree node) | [Optional] Admin thêm Quận/Huyện, Phường/Xã | CAT-01 |
| 5 | catalog.md (Tab 2) | Admin chọn tab Loại BĐS/Phòng | CAT-02, CAT-03 |
| 6 | catalog.md | [Optional] Admin quản lý Nội thất (add/edit/delete) | CAT-04 |
| 7 | catalog.md | [Optional] Admin quản lý Tiện ích (add/edit/delete) | CAT-05 |
| 8 | catalog.md (dialog) | [Optional] Admin quản lý Dịch vụ (kèm giá) | CAT-06 |
| 9 | catalog.md (Tab 3) | Admin chuyển tab Phân quyền | USER-05 |

## 4. Alternate Flows
- **Xoá node địa giới có con**: Error "Vui lòng xoá đơn vị hành chính cấp dưới trước"
- **Tree rỗng**: Empty state "Không tìm thấy địa giới hành chính"
- **Trùng tên**: [ASSUMPTION] Validation "Tên này đã tồn tại" trong cùng cấp

## 5. Error Handling
- **Form thiếu trường**: Highlight field và thông báo lỗi
- **Xoá danh mục đang được sử dụng**: Warning "Danh mục này đang được sử dụng bởi BĐS/phòng. Bạn có chắc chắn muốn xoá?"
- **[ASSUMPTION] Cache invalidation**: Sau khi thay đổi catalog, cần refresh dữ liệu ở các form liên quan

## 6. Screens Involved
- catalog.md

## 7. Gaps
- [DESIGN GAP] CAT-07 (File) — không có màn hình quản lý file riêng; upload file được nhúng trong form BĐS/phòng
