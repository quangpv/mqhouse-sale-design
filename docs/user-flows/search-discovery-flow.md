# Luồng tìm kiếm và khám phá

## 1. Flow Overview
- **Flow name**: Luồng tìm kiếm và khám phá BĐS
- **Actor**: All users (logged in)
- **Description**: Quy trình tìm kiếm, lọc, xem bản đồ và xem chi tiết BĐS/phòng

## 2. Preconditions
- User đã đăng nhập
- Có dữ liệu BĐS trong hệ thống

## 3. Main Flow (Happy Path)
| Step | Screen | Action | Story ID |
|------|--------|--------|----------|
| 1 | dashboard.md | User nhập từ khoá tìm kiếm hoặc chọn category | SEARCH-01 |
| 2 | search.md | User xem kết quả tìm kiếm | SEARCH-01, SEARCH-02 |
| 3 | search.md (bottom sheet) | [Optional] User mở filter → áp dụng bộ lọc nâng cao | SEARCH-02 |
| 4 | map.md | [Optional] User chuyển qua Map View → xem marker | MAP-01, MAP-02 |
| 5 | map.md | [Optional] User kéo radius slider → tìm trong bán kính | MAP-03 |
| 6 | map.md (bottom sheet) | [Optional] User xem danh sách BĐS trong bottom sheet | MAP-04 |
| 7 | property-detail.md | User tap vào BĐS → xem chi tiết | BDS-02 |
| 8 | room-detail.md | User tap vào phòng → xem chi tiết phòng | PHONG-02 |

## 4. Alternate Flows
- **Không có kết quả**: Empty state trên search hoặc map — "Không tìm thấy BĐS phù hợp"
- **Lọc lại**: User điều chỉnh filter và áp dụng lại
- **Lưu bộ lọc**: [DESIGN GAP] SEARCH-03 — chưa có UI lưu filter
- **Tìm kiếm nâng cao**: [ASSUMPTION] Filter bottom sheet có các tiêu chí: khoảng giá, diện tích, số phòng, loại hình, quận/huyện

## 5. Error Handling
- **Location không được cấp quyền**: Toast "Vui lòng cấp quyền truy cập vị trí"
- **Map không tải được**: Fallback về danh sách + retry button
- **Kết quả tìm kiếm quá nhiều**: [ASSUMPTION] Pagination hoặc infinite scroll (20 items/page)
- **[ASSUMPTION] Search timeout**: Nếu API không phản hồi sau 10s → hiển thị "Tìm kiếm đang mất nhiều thời gian hơn dự kiến"

## 6. Screens Involved
- dashboard.md
- search.md
- map.md
- property-detail.md
- room-detail.md

## 7. Gaps
- [DESIGN GAP] SEARCH-03 (Lưu bộ lọc tìm kiếm) — chưa có UI
