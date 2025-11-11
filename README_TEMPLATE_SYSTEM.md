# 게이트맨 웹사이트 - 템플릿 시스템 사용 가이드

## 템플릿 시스템이란?

WordPress처럼 헤더와 푸터를 한 곳에서만 수정하면 모든 페이지에 자동으로 적용되는 시스템입니다.

## 파일 구조

```
GATEMAN/
├── includes/
│   ├── header.html     ← 모든 페이지의 헤더 (여기만 수정하세요!)
│   └── footer.html     ← 모든 페이지의 푸터 (여기만 수정하세요!)
├── js/
│   └── load-template.js  ← 자동 로드 스크립트
├── index.html            ← 메인 페이지
├── smartdoorlock.html
├── technology.html
└── products/
    ├── gm-900s.html
    └── ... (19개 제품 페이지)
```

## 로컬 테스트 방법

### 방법 1: 배치 파일 실행 (가장 쉬움)

1. `start_server.bat` 파일을 더블클릭
2. 명령 프롬프트 창이 열리면서 서버 시작
3. 브라우저에서 `http://localhost:8080/index.html` 접속
4. 테스트 완료 후 명령 프롬프트 창 닫기

### 방법 2: 명령어로 실행

```bash
cd C:\Users\ASDS\Desktop\GATEMAN
python -m http.server 8080
```

브라우저에서 `http://localhost:8080/index.html` 접속

### 방법 3: Chrome을 특수 모드로 실행 (file:// 프로토콜)

Chrome 바로가기 속성에서 대상 끝에 추가:
```
--allow-file-access-from-files
```

예시:
```
"C:\Program Files\Google\Chrome\Application\chrome.exe" --allow-file-access-from-files
```

## 실제 배포 (웹 호스팅)

### 구글 호스팅 / 일반 웹 호스팅

전체 GATEMAN 폴더를 서버에 업로드하면 **자동으로 작동**합니다!

- FTP로 업로드
- GitHub Pages
- Netlify
- Vercel
- 구글 Firebase Hosting

**서버에 올리면 아무 설정 없이 100% 작동합니다!**

## 헤더/푸터 수정 방법

### 1. 헤더 수정

`includes/header.html` 파일만 수정하세요.

예: 전화번호 변경
```html
<span>010-6633-7732</span>  ← 이 부분만 수정
```

저장 후 브라우저 새로고침하면 **모든 25개 페이지**에 자동 적용!

### 2. 푸터 수정

`includes/footer.html` 파일만 수정하세요.

### 3. 메뉴 추가

`includes/header.html`의 nav 섹션:
```html
<nav class="main-nav">
    <ul>
        <li><a href="smartdoorlock.html">스마트도어락</a></li>
        <li><a href="technology.html">테크놀로지</a></li>
        <!-- 여기에 새 메뉴 추가 -->
        <li><a href="newpage.html">새 메뉴</a></li>
    </ul>
</nav>
```

## 장점

### ✅ 한 번만 수정
- 헤더 수정: `includes/header.html` 1개 파일만
- 푸터 수정: `includes/footer.html` 1개 파일만
- 25개 페이지 모두 자동 업데이트!

### ✅ 일관성 보장
- 모든 페이지가 100% 동일한 헤더/푸터
- 실수로 다르게 만들 위험 0%

### ✅ 유지보수 편함
- 전화번호 변경: 1곳만 수정
- 메뉴 추가: 1곳만 수정
- 로고 변경: 1곳만 수정

### ✅ 프로페셔널
- WordPress처럼 전문적인 구조
- 대형 사이트도 쉽게 관리

## 문제 해결

### 헤더/푸터가 보이지 않음 (로컬 file://)

**원인**: 브라우저 보안 정책
**해결**:
1. `start_server.bat` 실행 후 `http://localhost:8080` 사용
2. 또는 Chrome을 `--allow-file-access-from-files` 플래그로 실행

### 서버에 업로드했는데 작동 안함

**체크리스트**:
- [ ] `includes/` 폴더가 업로드되었나?
- [ ] `js/load-template.js` 파일이 있나?
- [ ] 브라우저 콘솔(F12)에서 에러 확인

### 경로 문제

모든 경로는 자동으로 조정됩니다:
- 루트 페이지: `./includes/header.html`
- 제품 페이지: `../includes/header.html`

## 작동 원리

```html
<!-- 각 HTML 페이지 -->
<div id="header-placeholder"></div>  ← 여기에 헤더가 자동 주입됨

<script src="js/load-template.js"></script>  ← 이 스크립트가 자동 처리
```

JavaScript가:
1. `includes/header.html` 파일 로드
2. `header-placeholder`에 내용 주입
3. 경로 자동 변환 (`/index.html` → `./index.html`)

## 지원

문제가 있으면:
1. 브라우저 콘솔(F12) 확인
2. `start_server.bat`로 로컬 테스트
3. 서버 업로드 시 자동 작동 확인
