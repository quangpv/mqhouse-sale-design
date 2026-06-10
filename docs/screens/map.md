# Map

## 1. Screen Overview
- **Screen name**: Map (Bản đồ)
- **Purpose**: Visualize real estate properties on a map with interactive markers, radius search, and collapsible result bottoms sheet.
- **Business context**: Provides spatial discovery of properties. Supports filtering by status, room type, property type, price, and amenities while viewing locations geographically.

## 2. UI Structure
### Layout sections
- **Full-screen Google Maps container** (`#gmap`): Custom styled map with POI/transit labels disabled.
- **Top transparent overlay**: Back button → Search, search input (default "Bình Thạnh, TP.HCM"), filter button.
- **Quick filter toolbar**: Glassmorphism pills (backdrop-blur-sm):
  - Trạng thái: dropdown (Còn hàng / Hết hàng)
  - Loại phòng: dropdown (Studio / 1PN / 2PN)
  - Loại hình BDS: dropdown (Căn hộ / Tòa nhà / Phòng trọ)
  - Giá thuê: → opens modalPrice
  - Tiện ích: → opens modalAmenities
- **My Location button**: Floating bottom-right, locate icon, pans to default coordinates (10.805, 106.715).
- **Bottom sheet results**: Collapsible sheet (110px default, 420px expanded) with drag handle, header "Kết quả (N sản phẩm)", and scrollable property card list.
- **Filter modals**:
  - modalDetail: Same structure as Search filter bottom sheet.
  - modalPrice: Dual-range slider for price.
  - modalAmenities: Amenity chip toggles.
- **Map markers**: Custom `OverlayView` with price labels + property type icons; selected state with scale/color change.

### Components
- **MapMarkerOverlay**: Custom Google Maps OverlayView showing price badge and property icon.
- **MyLocationOverlay**: Animated ping/pulse circles at user location.
- **Collapsible bottom sheet**: Drag handle, snap points (110px, 420px).
- **Glassmorphism filter pills**: Backdrop blur with dropdown menus.
- **Filter modal sheets**: Full-screen modal overlays for detail/price/amenities.

### Important UI patterns
- Haversine distance calculation for radius-based filtering.
- Custom OverlayView for map markers instead of standard markers (for branded price labels).
- Glassmorphism (backdrop-filter: blur) for toolbar overlay on map.
- Animated pulse for "My Location" indicator.

## 3. Entry Points
- Search → Map icon button.

## 4. States
- **Loading**: Map container shows spinner overlay while `initMap()` loads Google Maps API. Markers appear after data fetch.
- **Empty**: Map loads at default coordinates; bottom sheet shows "Không có kết quả trong khu vực này."
- **Error**: Toast "Không thể tải bản đồ. Vui lòng thử lại." if Google Maps API fails. Fallback message if location permission denied.
- **Success**: Map rendered with markers, bottom sheet populated with property cards.

## 5. Business Rules
### Validation rules
- Price range: Min ≤ Max, both within defined bounds.
- Radius: 0–50 km, default 5 km.
- Location permission: Required for "My Location" feature; if denied, default to Bình Thạnh coordinates.

### Permission rules
- All authenticated users can view the map.
- [ASSUMPTION] Geolocation API requires user permission (browser prompt).

### Conditional rendering rules
- My Location button hidden if geolocation is unavailable or denied.
- Marker selected state (scale + color change) on tap.
- Bottom sheet expands to 420px on card click or marker selection.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| MAP-01 | Xem bản đồ BDS | Planned |
| MAP-02 | Marker BDS | Planned |
| MAP-03 | Tìm kiếm theo bán kính | Planned |
| MAP-04 | Bottom sheet chi tiết BDS | Planned |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Map | Search | Back button |
| Map | Property Detail | Property card click / marker click |
| Map | Room Detail | Room card (multi-property) |
| Map | Sharing | Share button |

## 8. Mapping Notes
- Google Maps API is loaded via external script; requires API key.
- 7 mock properties with lat/lng in Bình Thạnh district for testing.
- [DESIGN GAP] No direction/routing feature from map to property location.
- [DESIGN GAP] No cluster marker support for large datasets — potential performance issue with 50+ markers.
- Filter state is independent of Search filter state (no sync between screens).
