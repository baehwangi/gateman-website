// 헤더/푸터 자동 로드 스크립트
(function() {
    // 현재 페이지의 경로 깊이 계산
    function getBasePath() {
        const path = window.location.pathname;

        // products 폴더 안에 있으면 ../ 사용
        if (path.includes('/products/') || path.includes('\\products\\')) {
            return '../';
        }
        return './';
    }

    const basePath = getBasePath();

    // XMLHttpRequest를 사용하여 파일 로드 (file:// 프로토콜 지원)
    function loadTemplate(url, placeholderId) {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200 || xhr.status === 0) { // status 0은 file:// 프로토콜
                    let html = xhr.responseText;

                    // 경로 수정 (절대경로 -> 상대경로)
                    html = html.replace(/href="\/([^"]+)"/g, `href="${basePath}$1"`);
                    html = html.replace(/src="\/([^"]+)"/g, `src="${basePath}$1"`);

                    const placeholder = document.getElementById(placeholderId);
                    if (placeholder) {
                        placeholder.innerHTML = html;
                    }
                } else {
                    console.error('템플릿 로드 실패:', url, 'Status:', xhr.status);
                }
            }
        };
        xhr.send();
    }

    // 헤더 로드
    loadTemplate(basePath + 'includes/header.html', 'header-placeholder');

    // 푸터 로드
    loadTemplate(basePath + 'includes/footer.html', 'footer-placeholder');
})();
