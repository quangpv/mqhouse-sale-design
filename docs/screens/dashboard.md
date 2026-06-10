# Dashboard

## 1. Screen Overview
- **Screen name**: Dashboard (Trang chủ)
- **Purpose**: Landing screen showing overview of real estate listings, featured properties, latest listings, and recently viewed properties.
- **Business context**: Serves as the main entry point after login. Provides quick access to search, property details, and new property registration.

## 2. UI Structure
### Layout sections
- **Top search bar**: Search icon + input field (placeholder "Tìm kiếm địa chỉ..."), Enter triggers search; "+" plus button navigates to addProperty.
- **Category grid**: 3-column grid (Căn hộ, Tòa nhà, Phòng trọ) with icons — all navigate to Search with pre-filtered type.
- **Banner slider**: 3 slides auto-rotating (4s interval) with dot indicators:
  - "Dịch vụ đăng tin BDS chuyên nghiệp" — property advertising
  - "Cho thuê văn phòng & mặt bằng" — office/space rental
  - "Nhà đất giá tốt mỗi ngày" — daily deals
- **Quick search section**: "Tìm kiếm nhanh" with province selector button (opens bottom sheet with all 63 provinces) and district filter chips (Quận 1, 2, 3, 4, 7, Bình Thạnh).
- **Featured section "Nổi bật"**: Horizontal scrollable cards (3 items: Flora Novia, Vinhomes Central Park, Sunrise City View).
- **Latest section "Mới nhất"**: Horizontal scrollable cards (3 items).
- **Recent section "Xem gần đây"**: Vertical row list (5 properties).

### Components
- **Property card**: Image, type badge, title, address, price, heart button (favorite), status indicator (green = Còn phòng, grey = Hết phòng).
- **Banner card**: Full-width image with overlay text, click → search.
- **Category card**: Icon + label, click → search with type filter.
- **Province bottom sheet**: Scrollable list of all 63 Vietnamese provinces.
- **District chips**: Horizontal scrollable pill buttons.

### Important UI patterns
- Horizontal scroll for card sections (Featured, Latest).
- Vertical stack for Recent section.
- Bottom sheet for province selection.

## 3. Entry Points
- Login → Dashboard (default landing screen).

## 4. States
- **Loading**: Skeleton cards while fetching properties (Featured, Latest, Recent).
- **Empty**: "Chưa có bất động sản nổi bật" / "Chưa có bất động sản mới" for each section. Recent section hides if empty.
- **Error**: Toast notification "Không thể tải dữ liệu. Vui lòng thử lại." with retry option.
- **Success**: Full dashboard with all sections populated.

## 5. Business Rules
### Validation rules
- Search input: Free text, minimum 2 characters to trigger search.
- Province selector: Exactly 1 province must be selected.
- District chips: Multiple selection allowed, all chips deselectable.

### Permission rules
- All authenticated (logged-in) users can view the dashboard.
- [ASSUMPTION] Guest users are redirected to Login.

### Conditional rendering rules
- Recent section ("Xem gần đây") only renders if the user has viewed at least one property in the current session.
- "+" button only visible if user has permission to create properties.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| DASH-01 | Xem tổng quan BDS | Planned |
| SEARCH-01 | Tìm kiếm cơ bản | Planned |
| BDS-02 | Xem chi tiết BDS (preview from card) | Planned |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Dashboard | Search | Search bar Enter / Categories / Banners / "Xem tất cả" |
| Dashboard | Add Property | "+" button |
| Dashboard | Property Detail | Property card click |

## 8. Mapping Notes
- All category clicks, banner clicks, and search submissions map to the Search screen with appropriate pre-filters.
- Province selector uses a bottom sheet identical in structure to the Search filter sheet's location selector.
- [DESIGN GAP] No pull-to-refresh mechanism defined; assumes auto-refresh on focus.
