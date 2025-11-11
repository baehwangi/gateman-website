# GATEMAN Products - Quick Reference Guide

## 📁 File Locations

**Base Directory:** `C:\Users\ASDS\Desktop\GATEMAN\products\`

## ✅ Completed Pages (4/14)

### 1. GM-1000L - Premium Flagship
**File:** `gm_1000l.html`
**URL:** `/products/gm_1000l.html`
**Features:** Motor lock, 0초 즉시잠김, 3-way customization, Quick Pass fingerprint
**Colors:** Black, Metallic Stone Gray

### 2. GM-900S - IoT Ready
**File:** `gm_900s.html`
**URL:** `/products/gm_900s.html`
**Features:** Dual Communication Pack included, Gateman Access, IPX4
**Colors:** Silver

### 3. G-SUIT scan - Triple Auth
**File:** `g_suit_scan.html`
**URL:** `/products/g_suit_scan.html`
**Features:** Fingerprint + Card + Password, Goodix module, Full-metal body
**Colors:** Modern Gold

### 4. G-CLICK scan - No-Drilling
**File:** `g_click_scan.html`
**URL:** `/products/g_click_scan.html`
**Features:** No-drilling installation, Perfect for rentals, 10x security
**Colors:** Dark Gray

## 📋 Remaining Pages (10/14)

### Premium Series (5)
- [ ] `gm_500s.html` - Slim black, fire-resistant (1,000°C)
- [ ] `gp_900d.html` - Push-pull with fingerprint, Dark Silver/Black
- [ ] `gp_700d.html` - Push-pull, no fingerprint, Dark Silver/Black
- [ ] `gp_500r.html` - 17mm ultra-slim, Modern Gold/Black
- [ ] `gp_500rc.html` - Cream limited edition, fire response

### G-SUIT Series (2)
- [ ] `g_suit_touch.html` - Metro Bronze, Card + Password
- [ ] `g_suit_simple.html` - Modern Gold, minimalist

### G-CLICK Series (1)
- [ ] `g_click_touch.html` - Dark Gray, no-drilling, Card + Password

### G-GRAB Series (2)
- [ ] `g_grab_touch.html` - Lever-type, Modern Gold, fingerprint
- [ ] `grab100_fh.html` - Lever-type scan+, Modern Gold

## 🎨 Design Elements

### Color Scheme
- **Primary Red:** #c8102e (GATEMAN brand color)
- **Dark Background:** #1a1a1a to #2d2d2d gradient
- **Light Background:** #f8f9fa
- **Text:** #1a1a1a (dark), #fff (light)

### Typography
- **Headings:** 2.5rem (h1), 1.3rem (h3)
- **Body:** 1.1rem (tagline), standard for descriptions
- **Font:** System fonts (inherit from main CSS)

### Layout Grid
- **Product Hero:** 2 columns (image | info)
- **Features:** Auto-fit grid, min 280px
- **IoT Features:** Auto-fit grid, min 200px
- **Mobile:** Single column stack

## 📞 Contact Numbers

### Dealer (김해 공식 대리점)
**Primary:** 055-123-4567
**Use in:** All CTAs, header, footer

### ASSA ABLOY Korea (본사)
**A/S Support:** 1544-3232
**Product Inquiry:** 1577-1919
**Use in:** Footer only

## 🔗 Link Paths

From `/products/*.html` to main site:
```
../index.html           → Home
../smartdoorlock.html   → Products list
../technology.html      → Technology page
../cs_support.html      → Customer support
../purchase.html        → Purchase page
../gateman.html         → About GATEMAN
../css/style.css        → Main stylesheet
../js/main.js           → Main JavaScript
```

## 🖼️ Image URLs

### Pattern
```html
https://gateman.kr/uploads/product/[MODEL-NAME]_main.jpg
```

### Examples
- GM-1000L: `https://gateman.kr/uploads/product/GM-1000L_main.jpg`
- GM-900S: `https://gateman.kr/uploads/product/GM-900S_main.jpg`
- G-SUIT scan: `https://gateman.kr/uploads/product/G-SUIT-scan_main.jpg`

### Fallback
```html
onerror="this.src='https://via.placeholder.com/500x600?text=[MODEL]'"
```

## 📊 Product Data by Model

### GM-1000L
- **Type:** Premium Motor Lock
- **Auth:** Fingerprint (100) + Card (100) + Password
- **Special:** 3-way customization
- **Lock:** Motor lock + Hook mechanism
- **Price Range:** High-end

### GM-900S
- **Type:** IoT Smart Lock
- **Auth:** Fingerprint (100) + Card (100) + Password (100)
- **Special:** Dual Comm Pack included
- **Lock:** Hook mechanism
- **Price Range:** Mid-high

### GM-500S
- **Type:** Slim Profile Lock
- **Auth:** Card + Password
- **Special:** Fire-resistant, curved handle
- **Lock:** 0-second instant
- **Price Range:** Mid

### GP-900D
- **Type:** Push-Pull with Fingerprint
- **Auth:** Fingerprint (100) + Card (100) + Password
- **Special:** 1-second auto-lock
- **Lock:** Hook mechanism
- **Price Range:** Mid-high

### GP-700D
- **Type:** Push-Pull Digital
- **Auth:** Card (100) + Password
- **Special:** 1-second instant lock
- **Lock:** Hook mechanism
- **Price Range:** Mid

### GP-500R
- **Type:** Ultra-Slim Push-Pull
- **Auth:** Card (100) + Password
- **Special:** 17mm slim design
- **Lock:** 1-second instant
- **Price Range:** Mid

### GP-500RC
- **Type:** Ultra-Slim with Fire Response
- **Auth:** Card (100) + Password
- **Special:** Cream edition, auto-unlock at 60°C
- **Lock:** Fire response tech
- **Price Range:** Mid

### G-SUIT scan
- **Type:** Triple Auth Integrated Handle
- **Auth:** Fingerprint (100) + Card (100) + Password
- **Special:** Goodix module, full-metal
- **Lock:** Hook mechanism
- **Price Range:** High

### G-SUIT touch
- **Type:** Dual Auth Integrated Handle
- **Auth:** Card (100) + Password
- **Special:** Metro Bronze finish
- **Lock:** Hook mechanism
- **Price Range:** Mid-high

### G-SUIT simple
- **Type:** Minimalist Push-Pull
- **Auth:** Card + Password
- **Special:** Metal plate body
- **Lock:** Push-pull mechanism
- **Price Range:** Mid

### G-CLICK scan
- **Type:** No-Drilling Fingerprint
- **Auth:** Fingerprint + Card (100) + Password
- **Special:** No-drilling, rental-friendly
- **Lock:** Hook (10x stronger)
- **Price Range:** Mid-high

### G-CLICK touch
- **Type:** No-Drilling Digital
- **Auth:** Card + Password
- **Special:** No-drilling installation
- **Lock:** Hook mechanism
- **Price Range:** Mid

### G-GRAB touch
- **Type:** Lever-Type Fingerprint
- **Auth:** Fingerprint + Card + Password
- **Special:** Safe Handle Mechanism
- **Lock:** Dual hook
- **Price Range:** High

### G-GRAB scan+ (grab100_fh)
- **Type:** Lever-Type Quick Pass
- **Auth:** Fingerprint + Card + Password
- **Special:** Multi-module comm
- **Lock:** Dual hook (10x)
- **Price Range:** High

## 🎯 Key Selling Points by Category

### Security
- 0초/1초 즉시잠김 (Instant locking)
- 후크 메커니즘 (Hook mechanism - 10x stronger)
- 가짜 지문 방지 (Fake fingerprint prevention)
- 화재 대응 (Fire response technology)
- 타임락 (Time lock after failures)

### Convenience
- 퀵패스 지문인식 (Quick Pass fingerprint)
- 푸시풀 메커니즘 (Push-pull operation)
- 에티켓 모드 (Silent mode)
- 음성 안내 (Voice guidance)
- 배터리 1년 (1-year battery life)

### Technology
- IoT 연동 (Gateman Access app)
- 실시간 알림 (Real-time notifications)
- 원격 제어 (Remote control)
- 영상 인터폰 (Video intercom integration)
- Goodix 지문 모듈 (High-end fingerprint sensor)

### Design
- 프리미엄 풀메탈 (Premium full-metal)
- 일체형 손잡이 (Integrated handle)
- 다양한 컬러 (Multiple color options)
- 슬림 디자인 (17mm ultra-slim)
- 커스터마이징 (3-way customization)

## 🏠 Installation Types

### Standard Installation
- All GM/GP series
- All G-SUIT series
- Requires door modification
- Professional installation

### No-Drilling Installation
- G-CLICK scan
- G-CLICK touch
- Perfect for rentals
- No door damage
- Quick installation
- Reusable

### Lever-Type Installation
- G-GRAB touch
- G-GRAB scan+
- Lever handle design
- Safe Handle Mechanism
- Multi-module ready

## 📱 IoT Features

### Basic (All Models Compatible)
- Optional Dual Communication Pack
- Optional Access Connect module
- Gateman Access app control

### Included IoT (GM-900S)
- Dual Communication Pack included
- Gateman DOT tag (1 unit)
- Ready for immediate IoT use

### IoT Capabilities
- Real-time push notifications
- Remote lock/unlock
- Temporary password generation
- Entry/exit logs
- Family arrival alerts
- Guest password management
- Video intercom integration

## 🔧 Common Specifications

### Power
- **Battery:** AA (1.5V) alkaline × 4
- **Lifespan:** ~1 year (10 uses/day)
- **Emergency:** 9V backup terminal

### Capacities
- **Fingerprint:** 100 registrations (if equipped)
- **Card:** 100 cards
- **Password:** 100 codes (if applicable)

### Security Features
- Fake fingerprint prevention
- Decoy password entry
- Internal forced lock
- Tamper detection alarm
- Time lock (3 min after 5 failures)
- Fire-resistant materials

### Convenience Features
- Battery replacement alerts
- Voice guidance system
- Etiquette mode (silent)
- Emergency power terminal
- IPX4 waterproof (select models)

## 📝 Template Sections

Every product page includes:
1. ✅ Header with navigation
2. ✅ Product hero (image + info + CTAs)
3. ✅ Features grid (4-6 boxes)
4. ✅ Special sections (customization, IoT, etc.)
5. ✅ Specifications table
6. ✅ CTA section
7. ✅ Footer with contacts

## 🚀 Quick Creation Steps

1. **Copy template** (use gm_1000l.html or matching type)
2. **Update head** (title, description)
3. **Change product info** (name, model, tagline)
4. **Update highlights** (3-5 key features)
5. **Modify features** (4-6 feature boxes)
6. **Edit specs table** (dimensions, colors, etc.)
7. **Adjust special sections** (if needed)
8. **Update image URL** (model-specific)
9. **Save as** `[model].html`
10. **Test** links, responsive design

## 📌 Important Notes

- Always use `055-123-4567` for dealer contact
- Keep `1544-3232` and `1577-1919` for HQ only
- Use relative paths (`../`) for all internal links
- Include image fallbacks with `onerror`
- Maintain "김해 공식 대리점" branding
- Remove all Naver store links
- Test on mobile devices
- Verify all CTAs work

## 📖 Documentation Files

- **README.md** - Full implementation guide
- **IMPLEMENTATION_SUMMARY.md** - Comprehensive summary
- **QUICK_REFERENCE.md** - This file
- **product-template-style.css** - Shared styling

---

**Last Updated:** 2024-11-10
**Completed:** 4/14 products (28.5%)
**Status:** Foundation complete, ready for batch creation
