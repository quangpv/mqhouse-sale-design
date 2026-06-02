# MAP-03: Tìm kiếm theo bán kính

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **kéo thanh trượt để chọn bán kính tìm kiếm**, So that **tìm BĐS trong phạm vi mong muốn**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Range slider chọn bán kính (1km - 50km)
- [ ] Hiển thị vòng tròn bán kính trên bản đồ
- [ ] Tự động cập nhật marker khi thay đổi bán kính
- [ ] Hiển thị số lượng BĐS tìm thấy trong bán kính
- [ ] Có thể kéo điểm center để thay đổi vị trí trung tâm

## Technical Tasks

### Backend
- `GET /api/map/radius?lat&lng&radius_km` - BĐS trong bán kính

### Frontend
- Range slider component
- Vẽ vòng tròn bán kính trên Google Maps (Circle)
- Debounce update khi kéo slider
