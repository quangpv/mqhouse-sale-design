## PHONG-06: Duyệt đổi trạng thái phòng (Sale)

- **Tên:** Duyệt yêu cầu đổi trạng thái phòng
- **Role:** Admin, SuperAdmin, HouseHolder (chủ phòng), Manager (quản lý phòng)
- **Mô tả:** As a **Admin/SuperAdmin/HouseHolder/Manager**, I want **duyệt hoặc từ chối yêu cầu đổi trạng thái phòng từ Sale**, So that **kiểm soát việc thay đổi trạng thái**

**Priority:** High

**Acceptance Criteria:**
- [ ] Danh sách yêu cầu đổi trạng thái từ Sale
- [ ] Hiển thị: phòng, trạng thái cũ, trạng thái yêu cầu (chờ duyệt Y), người yêu cầu, thời gian
- [ ] Nút "Duyệt" → chuyển từ "chờ duyệt Y" → "Y" (cập nhật thông tin khách nếu có)
- [ ] Nút "Từ chối" → nhập lý do → chuyển về trạng thái cũ
- [ ] Thông báo cho Sale kết quả duyệt
- [ ] HouseHolder chỉ duyệt được yêu cầu cho phòng thuộc BĐS của mình
- [ ] Manager chỉ duyệt được yêu cầu trong khu vực quản lý

## Technical Tasks

### Backend
- Bảng `yeu_cau_doi_trang_thai` (id, phong_id, nguoi_yeu_cau, trang_thai_cu, trang_thai_moi, ly_do, trang_thai_duyet, nguoi_duyet, thoi_gian)
- `GET /api/requests/status-changes` - danh sách yêu cầu (có filter theo người duyệt)
- `PUT /api/requests/status-changes/:id/approve` - duyệt + cập nhật trạng thái phòng
- `PUT /api/requests/status-changes/:id/reject` - từ chối + lý do
- Admin|SuperAdmin: tất cả; HouseHolder: phòng BĐS mình; Manager: trong KV
- Gửi TB cho Sale khi được duyệt/từ chối

### Frontend
- Danh sách yêu cầu + approve/reject dialog + hiển thị trạng thái cũ→mới
