// Load header and footer components automatically
(function() {
    // Function to load HTML content using XMLHttpRequest (works with file:// protocol)
    function loadComponent(elementId, filePath) {
        var xhr = new XMLHttpRequest();
        xhr.open('GET', filePath, true);
        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200 || xhr.status === 0) { // 0 for local files
                    var element = document.getElementById(elementId);
                    if (element) {
                        element.innerHTML = xhr.responseText;
                    }
                } else {
                    console.error('Failed to load ' + filePath);
                }
            }
        };
        xhr.send();
    }

    // Load components when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', function() {
            loadComponent('header-placeholder', 'includes/header.html');
            loadComponent('footer-placeholder', 'includes/footer.html');
        });
    } else {
        loadComponent('header-placeholder', 'includes/header.html');
        loadComponent('footer-placeholder', 'includes/footer.html');
    }
})();
