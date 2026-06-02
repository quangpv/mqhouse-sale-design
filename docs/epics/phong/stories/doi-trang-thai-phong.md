## PHONG-05: Đổi trạng thái phòng

- **Tên:** Cập nhật trạng thái phòng
- **Role:** HouseHolder, Manager, Admin, Super Admin, Sale (cần duyệt)
- **Mô tả:** As a **người quản lý phòng**, I want **thay đổi trạng thái phòng**, So that **cập nhật tình trạng cho thuê thực tế**

**Priority:** High

**Acceptance Criteria:**
- [ ] 8 trạng thái: đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống
- [ ] Radio button / dropdown 8 trạng thái (room-detail.html)
- [ ] Admin|SuperAdmin|Manager|HouseHolder đổi trực tiếp (bất kỳ → bất kỳ)
- [ ] Sale đổi X → Y bất kỳ → phòng chuyển sang "chờ duyệt Y", cần duyệt
- [ ] Duyệt (bởi HouseHolder|Manager|Admin|SuperAdmin) → chuyển "chờ duyệt Y" → "Y"
- [ ] Từ chối → chuyển về trạng thái cũ
- [ ] Khi đổi sang "đã cọc" hoặc "đã thuê" → cần nhập thông tin khách
- [ ] Khi đổi sang "đang trống" → xóa thông tin khách hiện tại
- [ ] Ghi lại lịch sử thay đổi trạng thái

## Technical Tasks

### Backend
- Mở rộng enum trạng thái phòng: thêm `chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống`
- Bảng `lich_su_trang_thai_phong` (id, phong_id, trang_thai_cu, trang_thai_moi, nguoi_thay_doi, thoi_gian)
- Bảng `yeu_cau_doi_trang_thai` (id, phong_id, nguoi_yeu_cau, trang_thai_cu, trang_thai_moi, ly_do, trang_thai_duyet, nguoi_duyet, thoi_gian)
- `PUT /api/rooms/:id/status` - đổi trạng thái trực tiếp (Admin|SuperAdmin|Manager|HouseHolder)
- `POST /api/rooms/:id/request-status-change` - Sale gửi yêu cầu đổi trạng thái
- `GET /api/rooms/:id/status-history` - lịch sử
- `GET /api/rooms/:id/request-status` - kiểm tra trạng thái yêu cầu hiện tại
- Kiểm tra role: Admin|SuperAdmin|Manager|HouseHolder → trực tiếp; Sale → chờ duyệt

### Frontend
- Radio button / dropdown 8 trạng thái
- Customer info form (khi đổi sang đã cọc/đã thuê)
- Badge màu khác cho trạng thái chờ duyệt
