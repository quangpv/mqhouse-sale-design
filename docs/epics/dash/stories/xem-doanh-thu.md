# DASH-03: Dashboard doanh thu

- **Role:** Admin, Super Admin
- **Mô tả:** As a **Admin/Super Admin**, I want **xem thống kê doanh thu từ cho thuê phòng**, So that **đánh giá hiệu quả kinh doanh**

**Priority:** Low

**Acceptance Criteria:**
- [ ] Tổng doanh thu theo tháng/năm
- [ ] Biểu đồ đường doanh thu theo thời gian
- [ ] Top BĐS có doanh thu cao nhất
- [ ] Doanh thu theo khu vực
- [ ] Lọc theo khoảng thời gian

## Technical Tasks

### Backend
- Tạo view tổng hợp doanh thu từ bảng hợp đồng
- `GET /api/dashboard/revenue` - doanh thu tổng quan
- `GET /api/dashboard/revenue-by-property` - doanh thu theo BĐS
- `GET /api/dashboard/revenue-by-area` - doanh thu theo khu vực
- Chỉ Admin/Super Admin xem được doanh thu

### Frontend
- Component biểu đồ doanh thu
- Bộ lọc thời gian (date range picker)
- Top BĐS doanh thu cao (bảng xếp hạng)
