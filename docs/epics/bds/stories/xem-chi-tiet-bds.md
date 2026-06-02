# BDS-02: Xem chi tiết Bất động sản

- **Role:** Tất cả (kể cả không đăng nhập)
- **Mô tả:** As a **người dùng**, I want **xem chi tiết BĐS với đầy đủ thông tin và hình ảnh**, So that **đánh giá BĐS có phù hợp không**

**Priority:** High

**Acceptance Criteria:**
- [ ] Hiển thị: tên, giá, địa chỉ, mô tả, diện tích, loại BĐS
- [ ] Gallery hình ảnh (swipe/carousel, click phóng to)
- [ ] Thông tin chi tiết: số phòng ngủ, toilet, tầng, hướng nhà, năm xây dựng
- [ ] Thông tin: mặt tiền, đường vào, giấy tờ pháp lý
- [ ] Danh sách nội thất (icon + tên)
- [ ] Danh sách tiện ích (icon + tên + khoảng cách)
- [ ] Bản đồ nhỏ hiển thị vị trí BĐS
- [ ] Danh sách phòng trực thuộc (grid)
- [ ] Nút yêu thích, chia sẻ
- [ ] BĐS hiển thị trạng thái theo logic:
    - Chưa duyệt → "Chưa duyệt"
    - Hết hạn → "Hết hạn"
    - Đã duyệt:
        - Có phòng "đang trống" → "Còn trống"
        - Không có phòng "đang trống" nhưng có phòng "sắp trống" → "Sắp có phòng"
        - Còn lại → "Hết phòng"

## Technical Tasks

### Backend
- Query BĐS + JOIN: loại BĐS, hình ảnh, nội thất, tiện ích, phòng
- `GET /api/properties/:id` - chi tiết BĐS
- `GET /api/properties/:id/rooms` - danh sách phòng
- Tăng lượt xem (nếu có)

### Frontend
- Màn hình property-detail.html
- Image gallery/carousel component
- Mini map component
- Room grid component
- Nút yêu thích, chia sẻ
