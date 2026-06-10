# Luồng quản lý phòng

## 1. Flow Overview
- **Flow name**: Luồng quản lý phòng
- **Actor**: HouseHolder, Manager, Admin, Super Admin, Sale (with approval)
- **Description**: Quy trình thêm, xem, sửa, đổi trạng thái và quản lý phòng cho thuê

## 2. Preconditions
- BĐS đã tồn tại trong hệ thống
- User có quyền quản lý phòng của BĐS đó
- [ASSUMPTION] Các loại phòng và giá đã được cấu hình

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | property-detail.md | User xem danh sách phòng | BDS-02, PHONG-09 |
| 2 | add-property.md (sub-screen) | User thêm phòng mới | PHONG-01 |
| 3 | room-detail.md | User xem thông tin phòng | PHONG-02 |
| 4 | room-detail.md | User mở status drawer → chọn trạng thái mới | PHONG-05 |
| 5 | — | [Nếu Sale] Chuyển sang trạng thái chờ duyệt | PHONG-06 |
| 6 | — | Manager/Admin nhận yêu cầu → duyệt/từ chối | PHONG-06 |
| 7 | room-detail.md | [Nếu "Đã cọc"] User nhập thông tin khách | PHONG-07 |
| 8 | — | [Nếu "Đã cho thuê"] User quản lý hợp đồng | PHONG-08 |
| 9 | room-detail.md | User sửa thông tin phòng | PHONG-03 |

## 4. Alternate Flows
- **Thay đổi trạng thái bị từ chối**: Admin từ chối → phòng giữ nguyên trạng thái cũ, thông báo cho Sale
- **Xoá phòng**: Soft delete với cascade confirmation → PHONG-04
- **Sale đổi trạng thái phòng**: Trạng thái chuyển sang "Chờ duyệt" → Admin xem xét

## 5. Error Handling
- **Phòng đã có hợp đồng**: Không cho phép xoá hoặc đổi trạng thái nếu đang có khách thuê
- **Giá phòng không hợp lệ**: Validation "Giá phải lớn hơn 0"
- **[ASSUMPTION] Trùng số phòng**: Warning "Số phòng đã tồn tại trong BĐS này"

## 6. Screens Involved
- property-detail.md
- add-property.md
- room-detail.md

## 7. Gaps
- [DESIGN GAP] PHONG-08 (Contract management) — không có dedicated UI cho quản lý hợp đồng
- [DESIGN GAP] PHONG-06 (Approve status change) — tồn tại dưới dạng Admin action trong property-detail.md bottom sheet nhưng không có UI riêng
