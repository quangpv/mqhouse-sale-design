# MAP-01: Xem bản đồ BĐS

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **xem bản đồ với các marker BĐS**, So that **khám phá BĐS theo vị trí địa lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Tích hợp Google Maps API
- [ ] Hiển thị tất cả BĐS đã duyệt trên bản đồ
- [ ] Marker hiển thị giá hoặc icon theo loại BĐS
- [ ] Zoom in/out chuột và touch
- [ ] Marker cluster khi zoom xa (nhiều marker gần nhau)
- [ ] Tự động center theo vị trí người dùng (nếu cho phép)
- [ ] Chế độ xem: Map và Satellite

## Technical Tasks

### Backend
- Đảm bảo bảng BĐS có trường latitude, longitude, indexed
- `GET /api/map/properties?sw_lat&sw_lng&ne_lat&ne_lng` - BĐS trong khung bản đồ

### Frontend
- Màn hình map.html: Google Maps integration
- Marker components với custom icon
- Marker clustering (MarkerClusterer)
- Nút chuyển đổi Map/Satellite
