document.addEventListener('DOMContentLoaded', async () => {
    // Hamburger Menu
    const burger = document.querySelector('.burger');
    const navLinks = document.querySelector('.nav-links');

    if (burger && navLinks) {
        burger.addEventListener('click', () => {
            navLinks.classList.toggle('active');
            burger.classList.toggle('toggle');
        });
    }

    // News Scroll Buttons
    const scrollContainer = document.querySelector('.news-scroll');
    const scrollLeftBtn = document.querySelector('.scroll-left');
    const scrollRightBtn = document.querySelector('.scroll-right');

    // Fetch and Populate News
    try {


        if (scrollContainer) {
            scrollContainer.innerHTML = newsItems.map(item => `
                <div class="news-card">
                    <div class="news-date-label">${item.date}</div>
                    <img src="${item.image}" alt="${item.title}" class="news-image">
                    <h3 class="news-title">${item.title}</h3>
                    <p class="news-description">${item.description}</p>
                    <div class="news-meta">
                        <span class="news-date"><i class="fas fa-calendar-alt"></i> ${item.date}</span>
                    </div>
                </div>
            `).join('');
        }
    } catch (error) {
        console.error('Error loading news:', error);
    }

    // Scroll Button Logic
    if (scrollContainer && scrollLeftBtn && scrollRightBtn) {
        scrollLeftBtn.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: -300, behavior: 'smooth' });
        });

        scrollRightBtn.addEventListener('click', () => {
            scrollContainer.scrollBy({ left: 300, behavior: 'smooth' });
        });

        const updateButtonState = () => {
            scrollLeftBtn.disabled = scrollContainer.scrollLeft === 0;
            scrollRightBtn.disabled = scrollContainer.scrollLeft + scrollContainer.clientWidth >= scrollContainer.scrollWidth;
        };

        scrollContainer.addEventListener('scroll', updateButtonState);
        updateButtonState();
    }
});