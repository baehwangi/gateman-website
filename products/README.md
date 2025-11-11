# GATEMAN Product Detail Pages - Implementation Guide

## Overview
This directory contains individual product detail pages for GATEMAN smart door locks, adapted for the GATEMAN 김해 공식 대리점 website.

## Completed Products

### Premium Series
1. **GM-1000L** (gm_1000l.html) - COMPLETED
   - Premium motor lock with Quick Pass fingerprint recognition
   - 0-second instant locking
   - 3-way customization (brackets, handle bars, deco chips)
   - Colors: Black, Metallic Stone Gray

2. **GM-900S** (gm_900s.html) - COMPLETED
   - IoT-enabled with Dual Communication Pack included
   - Quick Pass fingerprint recognition
   - Silver color
   - IPX4 waterproof rating

### Products to Create

#### Premium Series (Remaining)
3. **GM-500S** (gm_500s.html)
   - Slim profile design
   - 0-second instant locking
   - Fire-resistant materials (1,000°C)
   - Black color
   - Curved ergonomic handle

4. **GP-900D** (gp_900d.html)
   - Push-pull digital door lock with fingerprint
   - 1-second auto-lock
   - Hook mechanism dual-locking
   - Colors: Dark Silver, Black
   - Dimensions: 74x380x80mm

5. **GP-700D** (gp_700d.html)
   - Push-pull digital door lock (without fingerprint)
   - 1-second instant locking
   - Hook mechanism
   - Colors: Dark Silver, Black

6. **GP-500R** (gp_500r.html)
   - Ultra-slim 17mm design
   - Push-pull type
   - Colors: Modern Gold, Black
   - 1-second instant locking

7. **GP-500RC** (gp_500rc.html)
   - Cream Limited Edition available
   - Fire response technology (auto-unlock at 60°C)
   - Colors: Modern Gold/Black, Cream
   - Ultra-slim 17mm design

#### G-SUIT Series
8. **G-SUIT Scan** (g_suit_scan.html)
   - Triple authentication: Fingerprint + Card + Password
   - Push-pull mechanism
   - Hook mechanism dual-lock
   - Modern Gold finish
   - Goodix fingerprint module (100 registrations)

9. **G-SUIT Touch** (g_suit_touch.html)
   - Card + Password authentication
   - Push-pull mechanism
   - Metro Bronze color
   - Premium metal body
   - IPX4 waterproof

10. **G-SUIT Simple+** (g_suit_simple.html)
    - Minimalist design
    - Modern Gold color
    - Push-pull system
    - Metal plate body
    - Card + Password authentication

#### G-CLICK Series
11. **G-CLICK Scan** (g_click_scan.html)
    - No-drilling installation (무타공)
    - Fingerprint + Card + Password
    - Dark Gray color
    - Perfect for rentals
    - Hook mechanism (10x stronger security)

12. **G-CLICK Touch** (g_click_touch.html)
    - No-drilling installation
    - Card + Password authentication
    - Dark Gray color
    - Push-pull mechanism

#### G-GRAB Series
13. **G-GRAB Touch** (g_grab_touch.html)
    - Lever-type design
    - Quick Pass fingerprint + Card + Password
    - Modern Gold with black base
    - Safe Handle Mechanism
    - Dual communication pack slots

14. **G-GRAB Scan+** (grab100_fh.html)
    - Lever-type with Quick Pass fingerprint
    - Modern Gold color
    - Dual hook mechanism
    - Multi-module communication
    - Rounded corners with metal frame

## Product Information Sources

All product information was fetched from official gateman.kr product pages:
- Premium Series: https://gateman.kr/gm_1000l, /gm_900s, /gm_500s, /gp_900d, /gp_700d, /gp_500r, /gp_500rc
- G-SUIT Series: https://gateman.kr/g_suit_scan, /g_suit_touch, /g_suit_simple
- G-CLICK Series: https://gateman.kr/g_click_scan, /g_click_touch
- G-GRAB Series: https://gateman.kr/g_grab_touch, /grab100_fh

## Template Structure

Each product page should follow this structure:

### 1. HTML Head
- Title: "[제품명] - 게이트맨 김해 공식 대리점"
- Meta description with key product features
- Links to ../css/style.css and Font Awesome
- Inline styles or link to product-template-style.css

### 2. Header Section
- GATEMAN logo with "김해 공식 대리점" badge
- Navigation: 스마트도어락 | 테크놀로지 | 고객지원 | 제품구매 | 게이트맨
- Contact: 055-123-4567
- Mobile menu button

### 3. Product Hero Section
- Product image (from gateman.kr or placeholder)
- Product name and model
- Product category/type
- Key tagline/description
- 3-5 product highlights with checkmarks
- CTA buttons: "상담 문의" (tel:055-123-4567) and "구매하기"

### 4. Features Section
- Section header: "주요 기능"
- 4-6 feature boxes in grid layout
- Each with icon, heading, and description
- Focus on: Security, Convenience, Technology, Safety

### 5. IoT Section (if applicable)
- Red gradient background
- Explain Gateman Access features
- Real-time notifications
- Remote control capabilities
- Guest password management

### 6. Specifications Table
- Model name
- Colors
- Dimensions (front body, main body)
- Power source
- Authentication methods
- Capacities (fingerprint, card, password)
- Security features
- Convenience features
- Package contents

### 7. CTA Section
- Heading: "[제품명] 설치 상담 받으세요"
- Subheading: "김해 지역 무료 출장 설치 | 전문 기술자 직접 시공"
- Phone CTA: 055-123-4567
- Online purchase button
- Service hours: 평일 09:00 - 18:00
- Service area: 김해 전 지역 출장 가능

### 8. Footer
- Company info: 게이트맨 김해 공식 대리점
- Contact numbers:
  - 제품문의: 055-123-4567 (대리점)
  - A/S: 1544-3232 (본사)
  - 본사문의: 1577-1919
- Service areas: 장유동, 내동, 삼계동, 부원동, 봉황동, 외동
- Copyright: © 2024 게이트맨 김해 공식 대리점

## Key Implementation Notes

### Image URLs
- Primary: Use gateman.kr URLs: `https://gateman.kr/uploads/product/[MODEL]_main.jpg`
- Fallback: Use placeholder with onerror attribute
- Example: `onerror="this.src='https://via.placeholder.com/500x600?text=[MODEL]'"`

### Link Paths
- All internal links use relative paths: `../`
- Examples:
  - `../index.html`
  - `../smartdoorlock.html`
  - `../css/style.css`
  - `../js/main.js`

### Phone Numbers
- Dealer contact: 055-123-4567 (김해 공식 대리점)
- A/S support: 1544-3232 (ASSA ABLOY 본사)
- Product inquiry: 1577-1919 (본사)

### Branding
- Always include "김해 공식 대리점" with GATEMAN logo
- Remove all Naver store links
- Remove other dealer links
- Keep manufacturer info: "ASSA ABLOY Korea"

## Product Feature Highlights by Category

### Security Features (Common)
- 0초/1초 즉시잠김 (Instant locking)
- 후크 메커니즘 (Hook mechanism)
- 가짜 지문 방지 (Fake fingerprint prevention)
- 허수 비밀번호 (Decoy password)
- 내부 강제잠금 (Internal forced lock)
- 파손 감지 알람 (Tamper alarm)
- 타임락 (Time lock after failed attempts)
- 화재 대응 (Fire response)

### Convenience Features (Common)
- 퀵패스 지문인식 (Quick Pass fingerprint)
- 푸시풀 메커니즘 (Push-pull mechanism)
- 음성 안내 (Voice guidance)
- 에티켓 모드 (Etiquette/silent mode)
- 배터리 교체 알림 (Battery replacement alert)
- 9V 비상 전원 (Emergency power terminal)

### IoT Features (Select Models)
- Gateman Access 앱 연동
- 실시간 알림 (Real-time notifications)
- 원격 제어 (Remote control)
- 임시 비밀번호 생성 (Temporary passwords)
- 방문자 관리 (Visitor management)
- 영상 인터폰 연동 (Video intercom integration)

## Status

**Completed:** 2/14 products
**Remaining:** 12 products

## Next Steps

1. Create remaining Premium series pages (GM-500S, GP-900D, GP-700D, GP-500R, GP-500RC)
2. Create G-SUIT series pages (Scan, Touch, Simple)
3. Create G-CLICK series pages (Scan, Touch)
4. Create G-GRAB series pages (Touch, Scan+)
5. Test all pages for:
   - Correct header/footer rendering
   - Working navigation links
   - Responsive design
   - Image loading
   - Phone number links

## File Naming Convention
- Use lowercase
- Use underscores for multi-word models
- Include .html extension
- Examples: `gm_1000l.html`, `g_suit_scan.html`, `grab100_fh.html`
