# SEARCH-04: Gợi ý tìm kiếm thông minh

- **Role:** Tất cả
- **Mô tả:** As a **người dùng**, I want **nhận gợi ý tìm kiếm dựa trên hành vi và xu hướng**, So that **khám phá được BĐS tiềm năng**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Gợi ý BĐS nổi bật (featured)
- [ ] Gợi ý BĐS xem nhiều
- [ ] Gợi ý BĐS mới đăng
- [ ] Gợi ý theo khu vực người dùng hay xem

## Technical Tasks

### Backend
- `GET /api/search/trending` - BĐS xu hướng
- `GET /api/search/suggestions` - gợi ý cá nhân hóa

### Frontend
- Suggestions panel dưới search bar
