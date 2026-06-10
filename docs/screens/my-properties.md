# My Properties

## 1. Screen Overview
- **Screen name**: My Properties (Bất động sản của tôi)
- **Purpose**: View and manage the user's own published properties and saved (favorited) listings.
- **Business context**: Personal property management hub. Users can see their listings at a glance, navigate to detail/edit, share, or favorite/unfavorite properties.

## 2. UI Structure
### Layout sections
- **Header**: Back button → Profile, title "Bất động sản của tôi", search icon, "+" button → Add Property.
- **Tab bar**: Segmented control with two tabs:
  - "Đã đăng" (Published) — user's own listings.
  - "Yêu thích" (Favorites) — saved properties.
- **Property card list**: Scrollable vertical list with:
  - Thumbnail with overlay count (for multi-image properties).
  - Type badge + status badge (color-coded: green = Còn phòng, red = Hết phòng, yellow = Chờ duyệt).
  - Title (truncated to 2 lines).
  - Address with pin icon.
  - Price.
  - Share button → Sharing.
  - Heart toggle (favorite).
- **Bottom sheet**: "Đăng tin mới" info sheet with confirmation/cancel buttons.

### Components
- **Property card**: Thumbnail, overlay count, type badge, status badge, title, address, price, share button, heart toggle.
- **Segmented tab control**: "Đã đăng" / "Yêu thích" with active indicator.
- **Empty state component**: Folder-open icon, descriptive text, "Đăng tin ngay" CTA button.
- **Bottom sheet (confirmation)**: "Đăng tin mới" info text + confirm/cancel actions.

### Important UI patterns
- Tab switching via `switchTab()` toggles between published and favorites lists.
- `renderListings()` dynamically populates the card list based on active tab and data.
- `toggleFavorite()` handles optimistic UI update + API call.

## 3. Entry Points
- Profile screen → "Bất động sản của tôi".

## 4. States
- **Loading**: Skeleton cards (3 placeholders) while fetching list.
- **Empty (Published)**: Folder-open icon + "Chưa có bất động sản nào. Hãy đăng tin ngay!" + "Đăng tin ngay" CTA → Add Property.
- **Empty (Favorites)**: Heart icon + "Chưa có bất động sản yêu thích nào."
- **Error**: Toast "Không thể tải danh sách. Vui lòng thử lại." with retry.
- **Success**: Property cards rendered in scrollable list.

## 5. Business Rules
### Validation rules
- No input validation on this screen (read-only list with delete/favorite actions).
- Share action requires a valid property ID.

### Permission rules
- User can only see their own published properties (not other users').
- Favorites tab is personal — user sees only their own saved properties.
- "+" button (Add Property) requires property creation permission.

### Conditional rendering rules
- Thumbnail overlay count only shown if property has 2+ images (e.g., "5+").
- Status badge color varies by status: green (Còn phòng), red (Hết phòng), yellow (Chờ duyệt / Pending).
- Empty state differs between Published tab and Favorites tab.
- Share button hidden if property is in draft/pending state.

## 6. Related User Stories
| ID | Title | Status |
|----|-------|--------|
| BDS-08 | Danh sách BDS của tôi | Planned |
| FAV-03 | Danh sách yêu thích | Planned |

## 7. Navigation
| From | To | Action |
|------|----|--------|
| My Properties | Profile | Back button |
| My Properties | Add Property | "+" button / Empty state CTA |
| My Properties | Property Detail | Card click |
| My Properties | Sharing | Share button |

## 8. Mapping Notes
- Heart toggle in favorites tab acts as "remove from favorites" (unfilled heart).
- Heart toggle in published tab acts as "add to favorites" (filled heart on tap).
- [DESIGN GAP] No edit/delete action on cards — user must navigate to Property Detail to edit or delete.
- [DESIGN GAP] No bulk selection or batch operations (e.g., delete multiple, change status).
- [STORY GAP] No pagination or load-more mechanism defined; assumes all properties load at once.
