# SEARCH-03: Lưu bộ lọc tìm kiếm yêu thích

- **Role:** Người dùng đã đăng nhập
- **Mô tả:** As a **người dùng đã đăng nhập**, I want **lưu bộ lọc tìm kiếm đang dùng**, So that **có thể tìm lại nhanh mà không cần thiết lập lại**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Nút "Lưu bộ lọc" trên kết quả tìm kiếm
- [ ] Đặt tên cho bộ lọc đã lưu
- [ ] Danh sách bộ lọc đã lưu trong trang cá nhân
- [ ] Click vào bộ lọc đã lưu → tự động áp dụng
- [ ] Xóa bộ lọc đã lưu

## Technical Tasks

### Backend
- Bảng `saved_search` (id, user_id, filter_json, name, created_at)
- `POST /api/search/saved-filters` - lưu bộ lọc
- `GET /api/search/saved-filters` - danh sách đã lưu
- `DELETE /api/search/saved-filters/:id` - xóa

### Frontend
- Dialog lưu bộ lọc, danh sách đã lưu
