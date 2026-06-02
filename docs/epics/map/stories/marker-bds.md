# MAP-02: Marker và popup thông tin

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **click vào marker để xem thông tin tóm tắt BĐS**, So that **biết được thông tin cơ bản trước khi xem chi tiết**

**Priority:** High

**Acceptance Criteria:**
- [ ] Click marker → hiển thị info window/popup
- [ ] Popup hiển thị: tên BĐS, giá, địa chỉ, hình ảnh thumbnail
- [ ] Popup hiển thị trạng thái (nếu còn phòng trống)
- [ ] Nút "Xem chi tiết" trong popup → chuyển đến chi tiết BĐS
- [ ] Marker được đánh dấu active khi click
- [ ] Đóng popup khi click ra ngoài

## Technical Tasks

### Backend
- `GET /api/map/property/:id/summary` - thông tin tóm tắt cho popup

### Frontend
- InfoWindow/ActionSheet component trên bản đồ
- Xử lý sự kiện click marker và đóng popup
