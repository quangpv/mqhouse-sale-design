# Room Detail (Chi tiết phòng)

## 1. Screen Overview
- **Screen name**: Chi tiết phòng
- **Purpose**: View full room information, update room status with customer details, navigate between rooms in the same property
- **Business context**: Operational screen for day-to-day room management — status changes, customer deposit capture, and cross-room navigation within a building

## 2. UI Structure
### Layout sections
- **Floating nav**: Back → Property Detail, Share → sharing intent, Heart (favorite toggle)
- **Image carousel**: 3-image slider with dot indicators
- **Heading bar**: Mã BĐS badge, Mã phòng badge, Trạng thái badge (color-coded), title, price, address
- **Basic info row**: Property type icon, Room type, Design style, Area (m²), Bathroom count — inline icon-labeled chips
- **Service fees**: Electricity, water, management fee badges
- **Utilities**: Furniture + Amenities chips + building structure tags
- **Contact card**: Person name, role, Phone button, Zalo button
- **Persistent bottom bar**: "Sơ đồ" (Room diagram) button + "Đổi trạng thái" button
- **Bottom sheets**:
  - **Status update**: Status radio buttons (color-coded), customer info fields (shown for Đã cọc / Đã cho thuê), customer image capture/upload, Close / Confirm
  - **Room diagram**: Full grid of all rooms in the parent property (4 columns), filterable by status / type, current room highlighted, click → navigate to that room's detail
- **JS entrypoints**: `toggleRoomFav()`, `openRoomDiagram()`, `revealRoomStatusDrawer()`, `commitRoomStatusUpdate()`, `navigateToRoom()`

### Components
- `floating-nav` (back, share, heart)
- `image-carousel` (3 slides, dot indicators)
- `badge` (Mã BĐS, Mã phòng, Trạng thái)
- `info-chip` (property type, room type, design style, area, bathroom)
- `service-fee-badge`
- `chip-group` (furniture, amenities)
- `contact-card`
- `bottom-bar`
- `bottom-sheet` / `status-drawer`
- `room-diagram-grid` (4 columns, filterable, current-room highlight)
- `image-capture` (customer photo)

### Important UI patterns
- Room diagram doubles as navigation hub — highlights current room, allows switching to any other room in the property
- Status update sheet mirrors the same pattern from property-detail (shared component)
- Color-coded status badges consistent with property-detail color scheme

## 3. Entry Points
- Search room list item click
- Map room card click
- Property Detail room grid → room card click
- Room diagram (from room-detail itself) → another room card click

## 4. States
- **Loading**: Skeleton for carousel, info rows, contact card
- **Empty**: N/A (room always belongs to a property)
- **Error**: API error toast; image load fallback
- **Success**: Full room render with all sections populated

### Room status states (color-coded badges)
| Status | Visual |
|--------|--------|
| Đang trống | Green |
| Sắp trống | Yellow/Orange |
| Đã cọc | Blue |
| Đã cho thuê | Red |

## 5. Business Rules
### Validation rules
- Customer info required when status changes to Đã cọc or Đã cho thuê
- Customer image required for deposit confirmation? [ASSUMPTION]
- Status transitions follow the same state machine as property-detail:
  ```
  Empty ──→ Deposited ──→ Rented
    │          │              │
    └── About-to-vacate ───────┘
  ```

### Permission rules
- Same as property-detail: Sale needs approval for status changes; Admin/Manager/HouseHolder can change directly
- Pending-approval variants shown in action sheet based on role

### Conditional rendering rules
- Customer info + image capture: visible only when target status = Đã cọc / Đã cho thuê
- "Đổi trạng thái" button: always visible in bottom bar
- Room diagram highlight: current room marked with distinct border/background

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| PHONG-02 | Xem chi tiết phòng | — |
| PHONG-05 | Đổi trạng thái phòng | — |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Room Detail | Property Detail | Back button |
| Room Detail | Sharing intent | Share button |
| Room Detail | Another Room Detail | Room diagram → click other room card |

## 8. Mapping Notes
- `room-detail.html` (624 lines) — single HTML with bottom-sheet-driven sub-flows
- Room diagram grid is shared / similar to property-detail's rooms overview but with navigation (click → navigateToRoom) instead of quick-action sheet
- Status update bottom sheet appears to be the same component used in property-detail
- [DESIGN GAP] **PHONG-08 (Quản lý hợp đồng)** has no dedicated UI — only status change with customer info capture exists, no contract document management or lifecycle
- [DESIGN GAP] **PHONG-09 (Danh sách phòng theo BDS)** — room grid exists within property-detail and room-detail but no standalone screen; always embedded
- [ASSUMPTION] Customer info captured during status update (Đã cọc / Đã cho thuê) serves as light contract record; full contract management is future scope
