# BDS-04: Xóa Bất động sản

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xóa BĐS không còn sử dụng**, So that **dọn dẹp dữ liệu hệ thống**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Chỉ Admin/Super Admin mới có quyền xóa
- [ ] Hiển thị confirm dialog trước khi xóa
- [ ] Xóa mềm (soft delete) - cập nhật trạng thái "đã xóa"
- [ ] Xóa kéo theo các phòng, hình ảnh, hợp đồng liên quan
- [ ] Thông báo cho chủ BĐS khi bị xóa
- [ ] Không cho xóa BĐS đang có hợp đồng hiệu lực

## Technical Tasks

### Backend
- Soft delete: UPDATE trạng thái, hoặc hard delete với CASCADE
- `DELETE /api/properties/:id` - xóa BĐS
- `GET /api/properties/:id/check-delete` - kiểm tra có thể xóa?
- Chỉ Admin/Super Admin
- Gửi thông báo cho chủ BĐS

### Frontend
- Confirm dialog + xử lý kết quả
