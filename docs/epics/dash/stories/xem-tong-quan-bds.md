# DASH-01: Dashboard tổng quan BĐS

- **Role:** Admin, Manager, HouseHolder
- **Mô tả:** As a **người quản lý**, I want **xem tổng quan số liệu BĐS trên Dashboard**, So that **nắm được tình hình BĐS đang quản lý**

**Priority:** High

**Acceptance Criteria:**
- [ ] Dashboard hiển thị các thẻ thống kê: Tổng BĐS, Đã duyệt, Chờ duyệt, Hết hạn
- [ ] Biểu đồ tròn phân loại theo trạng thái BĐS
- [ ] Biểu đồ cột BĐS mới theo tháng
- [ ] Danh sách BĐS gần hết hạn (5-10 items)
- [ ] Lọc theo khu vực (đối với Admin, Manager)
- [ ] Refresh dữ liệu định kỳ
- [ ] Xem được BĐS trong khu vực quản lý (Manager)

## Technical Tasks

### Backend
- Tạo view/materialized view tổng hợp thống kê BĐS
- `GET /api/dashboard/property-summary` - thống kê tổng quan
- `GET /api/dashboard/property-by-status` - phân loại theo trạng thái
- `GET /api/dashboard/property-by-month` - BĐS mới theo tháng
- `GET /api/dashboard/expiring-properties` - BĐS gần hết hạn
- Manager chỉ xem được BĐS trong khu vực quản lý

### Frontend
- Màn hình dashboard.html: card thống kê + biểu đồ (Chart.js/Recharts)
- Component biểu đồ tròn, biểu đồ cột
- Bảng danh sách BĐS gần hết hạn
