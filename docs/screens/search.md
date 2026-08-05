# Search

## 1. Screen Overview
- **Screen name**: Search (Tìm kiếm)
- **Purpose**: Browse, filter, and discover real estate properties. Supports basic keyword search and advanced multi-criteria filtering.
- **Business context**: Central discovery screen. All major entry points (dashboard, map back button) converge here. Largest and most feature-dense screen.

## 2. UI Structure
### Layout sections
- **Top sticky bar**: Search input (placeholder "Nhập tên bất động sản..."), map icon button → Map, advanced filter icon → opens filter bottom sheet.
- **Quick filter toolbar**: Horizontal scrollable dropdown buttons:
  - Trạng thái: Tất cả / Còn phòng / Hết phòng
  - Quận: Tất cả / Quận 1 / Quận 3 / Bình Thạnh
  - Loại phòng: Tất cả / Studio / 1 Phòng ngủ / 2 Phòng ngủ
  - Loại hình BDS: Tất cả / Căn hộ / Tòa nhà / Phòng trọ
  - Giá thuê: Tất cả / Dưới 5tr / 5tr - 10tr
  - Sắp xếp: Mặc định / Mới nhất / Giá tăng
- **Property result list**: Scrollable vertical list, two card variants:
  - `createCardSingle()`: single-room properties (1 image grid)
  - `createCardMulti()`: multi-room properties (2/3+ image grids)
- **Filter bottom sheet (modal)**: Detailed filters:
  - Trạng thái phòng: chip toggles
  - Loại phòng: chip toggles (Studio / 1PN / 2PN)
  - Kiểu phòng: dynamic chips from ROOM_DESIGN_STYLES
  - Loại hình BDS: chip toggles
  - Giá thuê: dual-range slider (0–100 Tr) + number inputs
  - Diện tích: dual-range slider (0–200 m²) + number inputs
  - Bán kính: single slider (0–50 km)
  - Số phòng vệ sinh: chip toggles (1 WC / 2 WC / 3+ WC)
  - Tiện ích cơ bản: amenity chips (Hồ bơi, Phòng gym, Bãi đậu xe, etc.)
  - Nội thất & Kết cấu: furniture chips
  - Bottom: "Xoá lọc" (Clear) and "Áp dụng" (Apply)
- **Room list bottom sheet**: For multi-room properties; rooms grouped by type/design style.

### Components
- **Property card (single)**: Text section on top — address, then row of (title + detail meta) left / price right (right-aligned, vertically centered) — image grid below with status badge overlay (top-left) and share/heart icon overlay (top-right, `bg-white/90`).
- **Property card (multi)**: Header with address, then title row with heart/share, horizontal scroll of room mini-cards (room-type abbrev badge, red bold price, "Còn N / Hết" availability overlay unchanged).
- **Room list bottom sheet**: Rooms grouped by type/design style; price red bold; room type kept in full name (not abbreviated).
- **Quick filter dropdown**: Scroll-aware positioning, click-outside close.
- **Filter bottom sheet**: Modal overlay with scrollable filter groups.
- **Range sliders**: Dual-handle (Giá, Diện tích), single-handle (Bán kính).
- **Chip toggles**: Multi-select pill buttons.

### Important UI patterns
- Client-side filtering with `filterState` object and `applyFilters()` function.
- Scroll-aware dropdown positioning for quick filters (avoids viewport clipping).
- Two card variants for single vs multi-room properties.
- Card layout: linear text-on-top / image-below; room-type name abbreviated via `abbrevRoomType()` (STD/1PN/2PN/DUP/SLP) on search cards only; price emphasized `text-h3 font-bold text-error`.
- Result list items separated by `divide-y divide-border` (no per-card border).

## 3. Entry Points
- Dashboard search bar / Categories / Banners.
- Map back button.

## 4. States
- **Loading**: Skeleton result cards (3–6 placeholders) while fetching.
- **Empty**: Illustration + "Không tìm thấy kết quả phù hợp" + suggestions to adjust filters.
- **Error**: Toast "Không thể tải kết quả. Vui lòng thử lại." with retry.
- **Success**: Property list with count "N kết quả".

## 5. Business Rules
### Validation rules
- Search input: Free text, minimum 2 characters.
- Price range: Min <= Max, both within 0–100 Tr.
- Area range: Min <= Max, both within 0–200 m².
- Radius: 0–50 km.

### Permission rules
- All authenticated users can search and view results.
- [ASSUMPTION] Guest users are redirected to Login.

### Conditional rendering rules
- Multi-room card variant only shown when property has >1 room.
- Room list bottom sheet only shown when clicking a multi-room property.
- Kiểu phòng (Design Style) chips are dynamic based on `ROOM_DESIGN_STYLES` data.
- Quick filter dropdowns close on click-outside.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| SEARCH-01 | Tìm kiếm cơ bản | Planned |
| SEARCH-02 | Tìm kiếm nâng cao | Planned |
| SEARCH-03 | Lưu bộ lọc tìm kiếm | Not planned |
| SEARCH-04 | Gợi ý tìm kiếm thông minh | Not planned |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Search | Map | Map icon button |
| Search | Property Detail | Single property card click |
| Search | Property Detail | Multi property card click → room list → detail |
| Search | Room Detail | Room item in room list sheet |
| Search | Sharing | Share button on card |

## 8. Mapping Notes
- [DESIGN GAP] SEARCH-03 (Lưu bộ lọc tìm kiếm) has no UI — no save/load filter preset mechanism exists.
- [DESIGN GAP] SEARCH-04 (Gợi ý tìm kiếm thông minh) has no UI — no autocomplete or suggested search terms.
- Filter state (`filterState`) is managed client-side; no persistence across sessions.
- The quick filter toolbar syncs with the filter bottom sheet — changing either updates both.
- Mock data includes 7 properties for testing filters.
