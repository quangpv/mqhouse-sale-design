# Luồng quản lý bất động sản

## 1. Flow Overview
- **Flow name**: Luồng quản lý bất động sản
- **Actor**: HouseHolder, Manager, Admin, Super Admin
- **Description**: Quy trình tạo, xem, sửa, duyệt và quản lý bất động sản

## 2. Preconditions
- User đã đăng nhập
- User có quyền tạo/sửa BĐS (role phù hợp)
- [ASSUMPTION] Dữ liệu catalog (địa giới, loại BĐS, tiện ích) đã được cấu hình

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | dashboard.md | User tap nút "+" (FAB) | DASH-01 |
| 2 | add-property.md | User điền form thông tin BĐS → lưu | BDS-01 |
| 3 | add-property.md (sub-screen) | User thêm các phòng trực thuộc | PHONG-01 |
| 4 | my-properties.md | User xem danh sách BĐS đã tạo | BDS-08 |
| 5 | property-detail.md | User xem chi tiết BĐS | BDS-02 |
| 6 | property-detail.md | [Nếu Admin] Mở bottom sheet → duyệt/từ chối | BDS-05 |
| 7 | add-property.md | User sửa BĐS (pre-filled form) | BDS-03 |

## 4. Alternate Flows
- **Lưu nháp**: BĐS ở trạng thái "Nháp", chưa hiển thị công khai
- **BĐS bị từ chối**: Gửi thông báo cho user → user sửa lại và gửi duyệt lại
- **BĐS hết hạn**: [DESIGN GAP] Admin review, gia hạn hoặc archive — BDS-06 chưa có HTML
- **Đánh dấu nổi bật**: [DESIGN GAP] Admin/SA gắn huy hiệu gold — BDS-07 chưa có HTML
- **Xoá BĐS**: [DESIGN GAP] Soft delete với cascade confirmation — BDS-04 chưa có delete UI trong property-detail.html

## 5. Error Handling
- **Form thiếu trường bắt buộc**: Highlight đỏ các field, hiển thị message lỗi cụ thể
- **Upload ảnh thất bại**: Toast "Tải ảnh lên thất bại", giữ nguyên form
- **BĐS trùng địa chỉ**: [ASSUMPTION] Warning "BĐS này đã tồn tại"
- **Network error khi submit**: Lưu local draft, cho phép retry

## 6. Screens Involved
- dashboard.md
- add-property.md
- my-properties.md
- property-detail.md

## 7. Gaps
- [DESIGN GAP] BDS-06 (Expiry) — không có HTML
- [DESIGN GAP] BDS-07 (Featured) — không có HTML
- [DESIGN GAP] BDS-04 (Delete) — không có delete UI trong property-detail.html
