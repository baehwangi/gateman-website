// Load header and footer components automatically
(function() {
    // Function to load HTML content
    function loadComponent(elementId, filePath) {
        fetch(filePath)
            .then(response => {
                if (!response.ok) {
                    throw new Error('Failed to load ' + filePath);
                }
                return response.text();
            })
            .then(html => {
                const element = document.getElementById(elementId);
                if (element) {
                    element.innerHTML = html;
                }
            })
            .catch(error => {
                console.error('Error loading component:', error);
            });
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