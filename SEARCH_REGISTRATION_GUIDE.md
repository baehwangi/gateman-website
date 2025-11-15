# 네이버/구글 검색 등록 완벽 가이드

현재 사이트: https://baehwangi.github.io/gateman-website

---

## 1️⃣ 네이버 서치어드바이저 등록

### Step 1: 사이트 등록

1. **네이버 서치어드바이저 접속**
   - URL: https://searchadvisor.naver.com
   - 네이버 계정으로 로그인

2. **웹마스터 도구 접속**
   - 상단 메뉴에서 "웹마스터 도구" 클릭

3. **사이트 추가**
   - "사이트 추가" 버튼 클릭
   - URL 입력: `https://baehwangi.github.io/gateman-website`
   - "추가" 버튼 클릭

### Step 2: 소유권 확인

네이버가 제공하는 3가지 방법 중 **HTML 파일 업로드**가 가장 쉽습니다:

**방법 A: HTML 파일 업로드 (추천)**

1. 네이버가 제공하는 HTML 파일 다운로드
   - 파일명 예: `naver1234567890abcdef.html`
   - 파일 내용: 빈 파일이거나 네이버 코드만 있음

2. 다운로드한 파일을 이 폴더에 복사:
   ```
   C:\Users\ASDS\Desktop\GATEMAN\
   ```

3. Git에 추가 및 배포:
   ```bash
   cd C:\Users\ASDS\Desktop\GATEMAN
   git add naver*.html
   git commit -m "Add Naver Search Advisor verification file"
   git push origin main
   ```

4. 약 1~2분 후 네이버에서 "소유확인" 버튼 클릭

**방법 B: HTML 메타 태그 (대안)**

네이버가 제공하는 메타 태그를 index.html에 추가:
```html
<meta name="naver-site-verification" content="여기에_네이버가_준_코드" />
```

### Step 3: 사이트맵 제출

1. 소유 확인 완료 후, 왼쪽 메뉴에서 **"요청" → "사이트맵 제출"** 클릭

2. 사이트맵 URL 입력:
   ```
   https://baehwangi.github.io/gateman-website/sitemap.xml
   ```

3. "확인" 버튼 클릭

### Step 4: 수집 요청 (선택사항)

중요한 페이지들을 직접 수집 요청:

1. 왼쪽 메뉴 **"요청" → "수집 요청"** 클릭

2. 중요한 페이지 URL 입력 (하루 최대 10개):
   ```
   https://baehwangi.github.io/gateman-website/index.html
   https://baehwangi.github.io/gateman-website/product.html
   https://baehwangi.github.io/gateman-website/technology.html
   https://baehwangi.github.io/gateman-website/cs_support.html
   ```

3. "확인" 버튼 클릭

---

## 2️⃣ Google Search Console 등록

### Step 1: 속성 추가

1. **Google Search Console 접속**
   - URL: https://search.google.com/search-console
   - 구글 계정으로 로그인

2. **속성 추가**
   - 왼쪽 상단 "속성 추가" 또는 "속성 선택" → "속성 추가" 클릭

3. **속성 유형 선택**
   - **"URL 접두어"** 선택 (추천)
   - URL 입력: `https://baehwangi.github.io/gateman-website`
   - "계속" 버튼 클릭

### Step 2: 소유권 확인

구글이 제공하는 여러 방법 중 **HTML 파일 업로드**가 가장 쉽습니다:

**HTML 파일 업로드 방법**

1. 구글이 제공하는 HTML 파일 다운로드
   - 파일명 예: `google1234567890abcdef.html`
   - 파일 내용: `google-site-verification: google1234567890abcdef.html`

2. 다운로드한 파일을 이 폴더에 복사:
   ```
   C:\Users\ASDS\Desktop\GATEMAN\
   ```

3. Git에 추가 및 배포:
   ```bash
   cd C:\Users\ASDS\Desktop\GATEMAN
   git add google*.html
   git commit -m "Add Google Search Console verification file"
   git push origin main
   ```

4. 약 1~2분 후 구글에서 "확인" 버튼 클릭

### Step 3: 사이트맵 제출

1. 소유권 확인 완료 후, 왼쪽 메뉴에서 **"Sitemaps"** (사이트맵) 클릭

2. "새 사이트맵 추가" 입력란에 입력:
   ```
   sitemap.xml
   ```
   (전체 URL 입력 안 해도 됨)

3. "제출" 버튼 클릭

### Step 4: URL 검사 및 색인 생성 요청

1. 상단 검색바에 URL 입력:
   ```
   https://baehwangi.github.io/gateman-website/index.html
   ```

2. "색인 생성 요청" 버튼 클릭

3. 중요한 페이지들 반복 (최대 10개 정도):
   - index.html
   - product.html
   - technology.html
   - cs_support.html

---

## 3️⃣ 확인 및 모니터링

### 검색 등록 확인 (1~2주 후)

**네이버 검색**
```
site:baehwangi.github.io/gateman-website
```

**구글 검색**
```
site:baehwangi.github.io/gateman-website
```

검색 결과가 나오면 성공! 🎉

### 일반 키워드 검색 (2~4주 후)

```
"김해 게이트맨"
"밀양 디지털도어락"
"김해 도어락 설치"
"게이트맨 김해 대리점"
```

### 네이버 서치어드바이저 모니터링

- **검색 노출**: 얼마나 많이 검색 결과에 노출되었는지
- **클릭수**: 몇 명이 클릭했는지
- **수집 현황**: 몇 개 페이지가 수집되었는지
- **오류**: 문제가 있는 페이지

### Google Search Console 모니터링

- **실적**: 클릭수, 노출수, CTR, 평균 게재순위
- **URL 검사**: 페이지별 색인 상태
- **커버리지**: 색인된 페이지 수
- **검색어**: 어떤 검색어로 유입되는지

---

## 4️⃣ 추가 최적화 팁

### 네이버 플레이스 등록 (매우 중요!)

1. https://place.naver.com 접속
2. "내 비즈니스 등록" 클릭
3. 사업자 정보 입력:
   - 상호명: 게이트맨 김해 밀양 대리점
   - 주소: 경남 김해시 주촌면 골든루트로 108-31
   - 전화번호: 010-6633-7732
   - 카테고리: 도어락 설치업
4. 사진 등록 (최소 10장):
   - 매장 외관
   - 제품 사진
   - 시공 사례
   - 인증서/자격증

**효과**: 네이버 지도 검색, 로컬 검색에서 상위 노출!

### 구글 마이 비즈니스 등록

1. https://www.google.com/business 접속
2. "지금 시작" 클릭
3. 사업체 정보 입력 (네이버와 동일하게)
4. 사진 등록

**효과**: 구글 지도, 로컬 검색 상위 노출!

### 네이버 블로그 작성

1. 네이버 블로그 개설
2. 주 1~2회 포스팅:
   - 도어락 설치 후기
   - 제품 리뷰
   - 설치 가이드
   - 자주 묻는 질문
3. 포스팅에 사이트 링크 삽입

**효과**: 백링크 증가, 검색 순위 상승!

---

## 5️⃣ 체크리스트

### 네이버 등록
- [ ] 네이버 서치어드바이저 가입
- [ ] 사이트 추가
- [ ] 소유권 확인 (HTML 파일 또는 메타 태그)
- [ ] sitemap.xml 제출
- [ ] 주요 페이지 수집 요청
- [ ] 네이버 플레이스 등록
- [ ] 네이버 블로그 개설

### 구글 등록
- [ ] Google Search Console 가입
- [ ] 속성 추가
- [ ] 소유권 확인 (HTML 파일)
- [ ] sitemap.xml 제출
- [ ] URL 검사 및 색인 요청
- [ ] 구글 마이 비즈니스 등록

### 확인
- [ ] 1주일 후: site: 검색 확인
- [ ] 2주일 후: 일반 키워드 검색 확인
- [ ] 매주: 네이버/구글 콘솔 모니터링

---

## 📞 도움말

### 문제 해결

**Q: 소유권 확인 파일을 업로드했는데 확인이 안 돼요**
A: 1~2분 정도 기다린 후 다시 시도. GitHub Pages 배포에 시간이 걸릴 수 있음.

**Q: 사이트맵이 제출되지 않아요**
A: URL 확인. 끝에 `/sitemap.xml`이 정확히 붙어있는지 확인.

**Q: 언제쯤 검색 결과에 나오나요?**
A:
- site: 검색: 1~2주
- 일반 키워드: 2~4주
- 상위 노출: 1~3개월 (콘텐츠와 백링크에 따라 다름)

**Q: 검색 순위를 올리려면?**
A:
1. 네이버 플레이스 등록 (필수!)
2. 네이버 블로그 운영
3. 정기적인 콘텐츠 업데이트
4. 백링크 구축
5. 사용자 후기 수집

---

## 🎯 빠른 시작 (5분)

```bash
# 1. 네이버 서치어드바이저 접속
https://searchadvisor.naver.com

# 2. 사이트 추가
URL: https://baehwangi.github.io/gateman-website

# 3. HTML 파일 다운로드 받아서 GATEMAN 폴더에 저장

# 4. Git 커밋
cd C:\Users\ASDS\Desktop\GATEMAN
git add naver*.html
git commit -m "Add Naver verification"
git push

# 5. 1분 대기 후 네이버에서 "소유확인" 클릭

# 6. 사이트맵 제출
https://baehwangi.github.io/gateman-website/sitemap.xml

# 완료! 🎉
```

---

**작성일**: 2025년
**사이트**: https://baehwangi.github.io/gateman-website
**연락처**: 010-6633-7732
