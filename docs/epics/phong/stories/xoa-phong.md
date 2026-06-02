## PHONG-04: Xóa phòng

- **Tên:** Xóa phòng
- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xóa phòng không còn sử dụng**, So that **dọn dẹp dữ liệu**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Chỉ Admin/Super Admin
- [ ] Confirm dialog
- [ ] Soft delete
- [ ] Không xóa phòng đang có hợp đồng hiệu lực

## Technical Tasks

### Backend
- `DELETE /api/rooms/:id`
- Admin/Super Admin

### Frontend
- Confirm dialog
