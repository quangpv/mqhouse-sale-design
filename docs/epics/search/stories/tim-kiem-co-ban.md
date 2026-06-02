# SEARCH-01: Tìm kiếm BĐS/phòng cơ bản

- **Role:** Tất cả (kể cả Khách hàng không cần đăng nhập)
- **Mô tả:** As a **người dùng**, I want **tìm kiếm BĐS/phòng bằng từ khóa**, So that **nhanh chóng tìm được BĐS/phòng mong muốn**

**Priority:** High

**Acceptance Criteria:**
- [ ] Ô tìm kiếm trên header/dashboard
- [ ] Gợi ý kết quả khi gõ (autocomplete)
- [ ] Tìm kiếm theo: tên BĐS, địa chỉ, tên phòng
- [ ] Kết quả hiển thị dạng danh sách có phân trang
- [ ] Highlight từ khóa trong kết quả
- [ ] Debounce input (300ms) tránh gọi API quá nhiều

## Technical Tasks

### Backend
- Tạo full-text search index trên bảng BĐS và Phòng
- `GET /api/search?q=keyword` - tìm kiếm cơ bản, phân trang
- `GET /api/search/suggest?q=keyword` - gợi ý khi gõ

### Frontend
- Search bar component với autocomplete dropdown
- Trang kết quả tìm kiếm
- Highlight từ khóa, phân trang
