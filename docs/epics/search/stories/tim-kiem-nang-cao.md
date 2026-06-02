# SEARCH-02: Tìm kiếm nâng cao với bộ lọc

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **lọc BĐS/phòng theo nhiều tiêu chí**, So that **tìm được BĐS phù hợp với nhu cầu cụ thể**

**Priority:** High

**Acceptance Criteria:**
- [ ] Bộ lọc: loại BĐS, loại phòng, khoảng giá, diện tích, số phòng ngủ
- [ ] Bộ lọc: nội thất, tiện ích, dịch vụ
- [ ] Bộ lọc: khu vực (Tỉnh/Quận/Phường)
- [ ] Bộ lọc: trạng thái phòng (đang trống, sắp trống)
- [ ] Kết hợp nhiều bộ lọc cùng lúc
- [ ] Reset bộ lọc
- [ ] Hiển thị số lượng kết quả tìm thấy

## Technical Tasks

### Backend
- Tối ưu query với nhiều JOIN và WHERE điều kiện
- `GET /api/search/advanced` - search nâng cao với query params
- `GET /api/search/filters` - lấy danh sách giá trị cho các bộ lọc

### Frontend
- Filter panel (có thể là slide-over hoặc modal)
- Range slider cho giá và diện tích
- Cascading dropdown cho địa giới HC
