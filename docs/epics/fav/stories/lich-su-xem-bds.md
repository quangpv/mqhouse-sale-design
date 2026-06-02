# FAV-04: Lịch sử xem BĐS

- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng**, I want **xem lịch sử các BĐS tôi đã xem**, So that **dễ dàng tìm lại BĐS đã quan tâm**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Danh sách BĐS đã xem (mới nhất trước)
- [ ] Tối đa 10 BĐS gần nhất
- [ ] Hiển thị: hình ảnh, tên, giá, thời gian xem
- [ ] Click → xem chi tiết

## Technical Tasks

### Backend
- Database: Bảng `lich_su_xem_bds`
- `POST /api/history/properties/:id` - ghi lịch sử
- `GET /api/history/properties` - danh sách (tối đa 10)

### Frontend
- Lịch sử xem (trong profile hoặc sidebar)
