# BDS-05: Duyệt Bất động sản

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **duyệt hoặc từ chối BĐS do HouseHolder/Manager tạo**, So that **đảm bảo chất lượng tin đăng**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách BĐS chờ duyệt
- [ ] Xem chi tiết BĐS trong luồng duyệt
- [ ] Nút "Duyệt" → trạng thái "đã duyệt"
- [ ] Nút "Từ chối" → hiển thị dialog nhập lý do → trạng thái "bị từ chối"
- [ ] Tự động gửi thông báo cho người tạo
- [ ] Duyệt nhiều BĐS cùng lúc (bulk approve)

## Technical Tasks

### Backend
- Cập nhật trạng thái BĐS, ghi lại người duyệt, thời gian
- `PUT /api/properties/:id/approve` - duyệt BĐS
- `PUT /api/properties/:id/reject` - từ chối + lý do
- `PUT /api/properties/bulk-approve` - duyệt hàng loạt
- `GET /api/properties/pending` - danh sách chờ duyệt
- Chỉ Admin/Super Admin
- Tự động gửi thông báo kết quả duyệt

### Frontend
- Tab BĐS chờ duyệt trong my-properties
- Approve/reject dialog
- Bulk select + bulk action
