// Main JavaScript for GATEMAN Gimhae Website

document.addEventListener('DOMContentLoaded', function() {
    // Mobile Menu Toggle
    const mobileMenuBtn = document.querySelector('.mobile-menu-btn');
    const mainNav = document.querySelector('.main-nav');

    if (mobileMenuBtn) {
        mobileMenuBtn.addEventListener('click', function() {
            mainNav.classList.toggle('active');
            this.querySelector('i').classList.toggle('fa-bars');
            this.querySelector('i').classList.toggle('fa-times');
        });
    }

    // Load Popular Products on Homepage
    if (document.getElementById('popularProducts')) {
        loadPopularProducts();
    }

    // Load Products by Category on Smart Door Lock Page
    if (document.getElementById('premiumProducts')) {
        loadProductsByCategory();
        setupCategoryFilter();
    }

    // Setup Product Modal
    setupProductModal();

    // Smooth Scroll for Anchor Links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            const href = this.getAttribute('href');
            if (href !== '#' && document.querySelector(href)) {
                e.preventDefault();
                document.querySelector(href).scrollIntoView({
                    behavior: 'smooth'
                });
            }
        });
    });

    // Technology Tabs Functionality
    setupTechnologyTabs();

    // FAQ Functionality
    setupFAQTabs();
    setupFAQAccordion();
});

// Technology Tabs
function setupTechnologyTabs() {
    const tabs = document.querySelectorAll('.tech-tab');
    const panels = document.querySelectorAll('.tech-panel');

    if (tabs.length === 0 || panels.length === 0) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const targetTab = this.getAttribute('data-tab');

            // Remove active class from all tabs and panels
            tabs.forEach(t => t.classList.remove('active'));
            panels.forEach(p => p.classList.remove('active'));

            // Add active class to clicked tab and corresponding panel
            this.classList.add('active');
            document.getElementById(targetTab).classList.add('active');
        });
    });
}

// Load Popular Products for Homepage
function loadPopularProducts() {
    const container = document.getElementById('popularProducts');
    if (!container) return;

    const popularProducts = productsData.filter(p => p.popular).slice(0, 6);

    container.innerHTML = popularProducts.map(product => `
        <div class="product-card" data-product-id="${product.id}">
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                ${product.popular ? '<span class="product-badge">인기</span>' : ''}
            </div>
            <div class="product-info">
                <div class="product-series">${product.series}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-desc">${product.description}</p>
                <div class="product-features">
                    ${product.features.slice(0, 3).map(f => `<span class="feature-tag">${f}</span>`).join('')}
                </div>
                <div class="product-footer">
                    <div class="product-price">${product.price}</div>
                    <button class="btn btn-primary btn-sm view-detail-btn">상세보기</button>
                </div>
            </div>
        </div>
    `).join('');

    attachProductCardListeners();
}

// Load Products by Category
function loadProductsByCategory() {
    const categories = {
        premiumProducts: 'premium',
        gsuitProducts: 'gsuit',
        gclickProducts: 'gclick',
        ggrabProducts: 'ggrab',
        pushpullProducts: 'pushpull',
        mortiseProducts: 'mortise',
        rimProducts: 'rim',
        wideProducts: 'wide',
        glassProducts: 'glass'
    };

    Object.entries(categories).forEach(([containerId, category]) => {
        const container = document.getElementById(containerId);
        if (!container) return;

        let products = productsData.filter(p => {
            if (category === 'pushpull') {
                return p.type === 'pushpull' && !['premium', 'gsuit', 'gclick', 'ggrab'].includes(p.category);
            }
            return p.category === category;
        });

        if (products.length === 0) {
            container.closest('.product-category').style.display = 'none';
            return;
        }

        container.innerHTML = products.map(product => createProductCard(product)).join('');
    });

    attachProductCardListeners();
}

// Create Product Card HTML
function createProductCard(product) {
    return `
        <div class="product-card" data-product-id="${product.id}">
            <div class="product-image">
                <img src="${product.image}" alt="${product.name}">
                ${product.popular ? '<span class="product-badge">인기</span>' : ''}
            </div>
            <div class="product-info">
                <div class="product-series">${product.series}</div>
                <h3 class="product-name">${product.name}</h3>
                <p class="product-desc">${product.description}</p>
                <div class="product-features">
                    ${product.features.slice(0, 3).map(f => `<span class="feature-tag">${f}</span>`).join('')}
                </div>
                <div class="product-footer">
                    <div class="product-price">${product.price}</div>
                    <button class="btn btn-primary btn-sm view-detail-btn">상세보기</button>
                </div>
            </div>
        </div>
    `;
}

// Setup Category Filter
function setupCategoryFilter() {
    const filterBtns = document.querySelectorAll('.filter-btn');

    filterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            // Update active button
            filterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            const category = this.dataset.category;

            // Show/hide product categories
            const productCategories = document.querySelectorAll('.product-category');

            if (category === 'all') {
                productCategories.forEach(cat => cat.style.display = 'block');
            } else {
                productCategories.forEach(cat => {
                    const categoryId = cat.querySelector('[id$="Products"]')?.id;
                    if (!categoryId) {
                        cat.style.display = 'none';
                        return;
                    }

                    const categoryMap = {
                        premium: 'premiumProducts',
                        gsuit: 'gsuitProducts',
                        gclick: 'gclickProducts',
                        ggrab: 'ggrabProducts',
                        pushpull: 'pushpullProducts',
                        mortise: 'mortiseProducts',
                        rim: 'rimProducts',
                        wide: 'wideProducts',
                        glass: 'glassProducts'
                    };

                    cat.style.display = categoryId === categoryMap[category] ? 'block' : 'none';
                });
            }

            // Scroll to first visible category
            const firstVisible = Array.from(productCategories).find(cat => cat.style.display !== 'none');
            if (firstVisible) {
                firstVisible.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });
}

// Attach Product Card Click Listeners
function attachProductCardListeners() {
    document.querySelectorAll('.product-card').forEach(card => {
        card.addEventListener('click', function(e) {
            if (e.target.closest('.view-detail-btn')) {
                e.preventDefault();
                const productId = this.dataset.productId;

                // Check if product detail page exists
                const detailPageFilename = checkProductDetailPage(productId);

                if (detailPageFilename) {
                    // Navigate to product detail page
                    window.location.href = `products/${detailPageFilename}.html`;
                } else {
                    // Fallback to modal
                    showProductModal(productId);
                }
            }
        });
    });
}

// Check if product detail page exists
function checkProductDetailPage(productId) {
    // Map product IDs to their detail page filenames
    const productPageMap = {
        'GM-1000L': 'gm_1000l',
        'GM-900S': 'gm_900s',
        'GM-500S': 'gm_500s',
        'GP-900D': 'gp_900d',
        'GP-700D': 'gp_700d',
        'GP-500R': 'gp_500r',
        'GP-500RC': 'gp_500rc',
        'GP-300R': 'gp_300r',
        'GP-300UN': 'gp_300un',
        'GSUIT-SCAN-PLUS': 'g_suit_scan',
        'GSUIT-TOUCH-PLUS': 'g_suit_touch',
        'GSUIT-SIMPLE-PLUS': 'g_suit_simple',
        'GCLICK-SCAN-PLUS': 'g_click_scan',
        'GCLICK-TOUCH-PLUS': 'g_click_touch',
        'GGRAB-TOUCH': 'g_grab_touch',
        'GGRAB-SCAN-PLUS': 'grab100_fh'
    };

    return productPageMap[productId] || null;
}

// Setup Product Modal
function setupProductModal() {
    const modal = document.getElementById('productModal');
    if (!modal) return;

    const closeBtn = modal.querySelector('.modal-close');

    if (closeBtn) {
        closeBtn.addEventListener('click', () => {
            modal.style.display = 'none';
        });
    }

    window.addEventListener('click', (e) => {
        if (e.target === modal) {
            modal.style.display = 'none';
        }
    });

    // Close on Escape key
    document.addEventListener('keydown', (e) => {
        if (e.key === 'Escape' && modal.style.display === 'block') {
            modal.style.display = 'none';
        }
    });
}

// Show Product Modal
function showProductModal(productId) {
    const modal = document.getElementById('productModal');
    if (!modal) return;

    const product = productsData.find(p => p.id === productId);
    if (!product) return;

    // Populate modal content
    document.getElementById('modalImage').src = product.image;
    document.getElementById('modalImage').alt = product.name;
    document.getElementById('modalTitle').textContent = product.name;
    document.getElementById('modalCategory').textContent = product.series;
    document.getElementById('modalPrice').textContent = product.price;
    document.getElementById('modalDescription').textContent = product.description;

    // Features
    const featuresHtml = `
        <h3>주요 기능</h3>
        <ul>
            ${product.features.map(f => `<li><i class="fas fa-check"></i> ${f}</li>`).join('')}
        </ul>
    `;
    document.getElementById('modalFeatures').innerHTML = featuresHtml;

    // Specs
    const specsHtml = `
        <h3>제품 사양</h3>
        <table class="specs-table">
            <tr>
                <th>인증 방식</th>
                <td>${product.specs.auth}</td>
            </tr>
            <tr>
                <th>색상</th>
                <td>${product.specs.color}</td>
            </tr>
            <tr>
                <th>배터리</th>
                <td>${product.specs.battery}</td>
            </tr>
            <tr>
                <th>IoT 지원</th>
                <td>${product.specs.iot}</td>
            </tr>
        </table>
    `;
    document.getElementById('modalSpecs').innerHTML = specsHtml;

    // Show modal
    modal.style.display = 'block';
    document.body.style.overflow = 'hidden';

    // Reset scroll on close
    modal.addEventListener('click', function closeHandler(e) {
        if (e.target === modal || e.target.classList.contains('modal-close')) {
            document.body.style.overflow = 'auto';
            modal.removeEventListener('click', closeHandler);
        }
    });
}

// Scroll to Top Button (if needed)
window.addEventListener('scroll', function() {
    const scrollBtn = document.getElementById('scrollTopBtn');
    if (scrollBtn) {
        if (window.pageYOffset > 300) {
            scrollBtn.style.display = 'block';
        } else {
            scrollBtn.style.display = 'none';
        }
    }
});

// Lazy Loading Images
if ('IntersectionObserver' in window) {
    const imageObserver = new IntersectionObserver((entries, observer) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const img = entry.target;
                if (img.dataset.src) {
                    img.src = img.dataset.src;
                    img.removeAttribute('data-src');
                    observer.unobserve(img);
                }
            }
        });
    });

    document.querySelectorAll('img[data-src]').forEach(img => {
        imageObserver.observe(img);
    });
}

// Form Validation (if forms exist)
document.querySelectorAll('form').forEach(form => {
    form.addEventListener('submit', function(e) {
        if (!this.checkValidity()) {
            e.preventDefault();
            e.stopPropagation();
        }
        this.classList.add('was-validated');
    });
});

// FAQ Tabs Functionality
function setupFAQTabs() {
    const tabs = document.querySelectorAll('.faq-tab');
    const contents = document.querySelectorAll('.faq-content');

    if (tabs.length === 0 || contents.length === 0) return;

    tabs.forEach(tab => {
        tab.addEventListener('click', function() {
            const targetCategory = this.getAttribute('data-category');

            // Remove active class from all tabs and contents
            tabs.forEach(t => t.classList.remove('active'));
            contents.forEach(c => c.classList.remove('active'));

            // Add active class to clicked tab and corresponding content
            this.classList.add('active');
            const targetContent = document.querySelector(`.faq-content[data-category="${targetCategory}"]`);
            if (targetContent) {
                targetContent.classList.add('active');
            }
        });
    });
}

// FAQ Accordion Functionality
function setupFAQAccordion() {
    const faqQuestions = document.querySelectorAll('.faq-question');

    faqQuestions.forEach(question => {
        question.addEventListener('click', function() {
            const faqItem = this.parentElement;
            const isActive = faqItem.classList.contains('active');

            // Close all FAQ items in the current category
            const currentContent = faqItem.closest('.faq-content');
            if (currentContent) {
                currentContent.querySelectorAll('.faq-item').forEach(item => {
                    item.classList.remove('active');
                });
            }

            // Toggle current item
            if (!isActive) {
                faqItem.classList.add('active');
            }
        });
    });
}

// Animate on Scroll
function animateOnScroll() {
    const elements = document.querySelectorAll('.animate-on-scroll');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('animated');
            }
        });
    }, {
        threshold: 0.1
    });

    elements.forEach(el => observer.observe(el));
}

// Initialize animations if elements exist
if (document.querySelector('.animate-on-scroll')) {
    animateOnScroll();
}

console.log('GATEMAN Gimhae Website - Initialized Successfully');
