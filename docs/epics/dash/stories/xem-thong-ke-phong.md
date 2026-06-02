# DASH-02: Dashboard thống kê phòng

- **Role:** Admin, Manager, HouseHolder
- **Mô tả:** As a **người quản lý**, I want **xem thống kê trạng thái phòng**, So that **biết được tỷ lệ lấp đầy và tình trạng phòng**

**Priority:** Medium

**Acceptance Criteria:**
- [ ] Biểu đồ tròn phân loại phòng theo trạng thái (đang trống, đã cọc, đã thuê, sắp trống, chờ duyệt cọc, chờ duyệt thuê, chờ duyệt sắp trống, chờ duyệt đang trống)
- [ ] Số liệu tổng số phòng, phòng trống, phòng đã cho thuê
- [ ] Tỷ lệ lấp đầy (occupancy rate)
- [ ] Lọc theo BĐS hoặc khu vực
- [ ] Click vào từng trạng thái → lọc danh sách phòng tương ứng

## Technical Tasks

### Backend
- `GET /api/dashboard/room-summary` - thống kê phòng tổng quan
- `GET /api/dashboard/room-by-status` - phân loại theo trạng thái
- `GET /api/dashboard/occupancy-rate` - tỷ lệ lấp đầy
- Manager chỉ xem được phòng trong khu vực

### Frontend
- Thẻ thống kê phòng trên dashboard
- Biểu đồ tròn trạng thái phòng
- Click filter theo trạng thái
