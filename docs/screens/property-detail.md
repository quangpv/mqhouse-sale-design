# Property Detail (Chi tiết BDS)

## 1. Screen Overview
- **Screen name**: Chi tiết BĐS
- **Purpose**: View full property information, manage rooms, approve/reject property, update room statuses
- **Business context**: Central hub for property operations — portfolio review, room-level status management, approval workflow, and customer deposit handling

## 2. UI Structure
### Layout sections
- **Floating nav**: Back → home, Share → sharing intent, Heart (favorite toggle)
- **Hero image slider**: 3-image carousel with dot indicators
- **Core info bar**: Mã BĐS badge, Loại badge, Trạng thái badge (pending/approved), title, price range, address with pin icon
- **Room info section** (expandable):
  - Total room count + status breakdown chips: Đang trống / Đã cọc / Đã cho thuê / Sắp trống
  - "+" chip → Add Property (add new room)
  - Room types sub-section with expandable design-style counts
  - Area chips
- **Service fees**: Electricity, water, management fee badges
- **Utilities**: Furniture + Amenities chips + building structure tags
- **Contact card**: Person name, role, Phone button, Zalo button
- **Persistent bottom bar**: "Sơ đồ phòng" button + "Duyệt" button (visible only for pending properties)
- **Bottom sheets**:
  - **Quick room update**: Status radio buttons (color-coded), customer info fields (shown for Đã cọc / Đã cho thuê), customer image capture/upload, Save / Cancel
  - **Rooms overview**: Filterable grid (4 columns), status + type filters, click → quick action sheet
- **Approve dialog**: Confirm property approval; on confirm updates badge + bottom bar

### Components
- `floating-nav` (back, share, heart)
- `image-carousel` (3 slides, dot indicators)
- `badge` (Mã BĐS, Loại, Trạng thái)
- `status-chip-group` (room status breakdown)
- `room-type-accordion` (expandable counts per design style)
- `service-fee-badge`
- `chip-group` (furniture, amenities)
- `contact-card` (name, role, phone, Zalo)
- `bottom-bar` (persistent, context-aware buttons)
- `bottom-sheet` / `action-sheet`
- `approve-dialog`
- `image-capture` (customer photo for deposits)
- `filter-grid` (rooms overview with status/type filters)

### Important UI patterns
- Expandable room summary section with inline status chips
- Color-coded status radio buttons (quick room update)
- Conditional customer info + photo capture for deposited/rented rooms
- Approve button visibility tied to property status + user role

## 3. Entry Points
- Dashboard card click
- Search result card click
- Map marker card click
- My Properties card click

## 4. States
- **Loading**: Skeleton for hero, info sections, room grid
- **Empty**: No rooms yet — room section shows empty state with "+" prompt
- **Error**: API error toast; image load fallback
- **Success**: Full property render with all sections populated

### Property status states
| Status | Badge | Bottom bar actions |
|--------|-------|--------------------|
| Draft | Draft | — |
| Pending | Pending | "Duyệt" button visible |
| Approved | Approved | No approve button |
| Rejected | Rejected | — |
| Expired | Expired | — |

## 5. Business Rules
### Validation rules
- Only pending properties can be approved/rejected
- Room status transitions with pending variants (see below)
- Favorite heart: toggle on/off, no other "nổi bật" mechanism

### Permission rules
| Action | Sale | HouseHolder | Manager | Admin | SA |
|--------|------|-------------|---------|-------|----|
| View | ✓ | ✓ | ✓ | ✓ | ✓ |
| Edit | ✗ | Own | Area | All | All |
| Approve | ✗ | ✗ | Area | ✓ | ✓ |
| Change room status directly | ✗ | ✓ | ✓ | ✓ | ✓ |
| Change room status (needs approval) | ✓ | ✗ | ✗ | ✗ | ✗ |

### Conditional rendering rules
- "Duyệt" button: visible only when property status = `pending` AND user has approve permission
- Customer info + image capture: visible only in quick-update sheet when new status = Đã cọc or Đã cho thuê
- Quick action sheet actions filtered by user role (Sale sees pending-approval variants)

### Room state machine
```
Empty ──→ Deposited ──→ Rented
  │          │              │
  └── About-to-vacate ───────┘
  (Each transition has a pending-approval variant for Sale role)
```

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| BDS-02 | Xem chi tiết BDS | — |
| BDS-05 | Duyệt BDS | — |
| PHONG-05 | Đổi trạng thái phòng | — |
| PHONG-06 | Duyệt đổi trạng thái phòng | — |
| PHONG-07 | Xác nhận đặt cọc | — |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| Property Detail | Home | Back button |
| Property Detail | Sharing intent | Share button |
| Property Detail | Room Detail | Room in rooms overview / quick action "eye" icon |
| Property Detail | Add Property (add room) | "+" room chip |
| Property Detail | (approve) | Confirm approve dialog → status update |

## 8. Mapping Notes
- `property-detail.html` (774 lines) — single HTML with bottom-sheet-driven sub-flows (no page navigation for room update or rooms overview)
- Room state machine includes 4 base states + 4 pending-approval variants (8 total), but UI only shows 4 base states; pending variants are role-filtered in the action sheet [ASSUMPTION]
- Customer image capture for deposits uses device camera / file upload
- [DESIGN GAP] **BDS-07 (Đánh dấu nổi bật)** has no dedicated UI — favorite heart exists but no featured/gold badge or toggle for "nổi bật" promotion
- [DESIGN GAP] **BDS-06 (Quản lý BDS hết hạn)** has no dedicated UI — expired status badge exists but no batch renewal/archival flow
