document.addEventListener("DOMContentLoaded", () => {
    const header = document.getElementById("siteHeader");
    const menuToggle = document.getElementById("menuToggle");
    const navigation = document.getElementById("mainNavigation");
    const overlay = document.getElementById("menuOverlay");
    const navLinks = document.querySelectorAll(".nav-link");
    const mobileBooking = document.querySelector(".mobile-booking");

    if (!header || !menuToggle || !navigation || !overlay) {
        return;
    }

    let previousFocus = null;

    // OPEN MENU
    function openMenu() {
        previousFocus = document.activeElement;

        menuToggle.classList.add("is-open");
        navigation.classList.add("is-open");
        overlay.classList.add("is-visible");

        document.body.classList.add("menu-open");

        menuToggle.setAttribute("aria-expanded", "true");
        menuToggle.setAttribute("aria-label", "Close navigation menu");
    }

    // CLOSE MENU
    function closeMenu(restoreFocus = false) {
        menuToggle.classList.remove("is-open");
        navigation.classList.remove("is-open");
        overlay.classList.remove("is-visible");

        document.body.classList.remove("menu-open");

        menuToggle.setAttribute("aria-expanded", "false");
        menuToggle.setAttribute("aria-label", "Open navigation menu");

        if (restoreFocus) {
            menuToggle.focus();
        }
    }

    // HAMBURGER BUTTON
    menuToggle.addEventListener("click", () => {
        if (navigation.classList.contains("is-open")) {
            closeMenu();
        } else {
            openMenu();
        }
    });

    // CLOSE ON OVERLAY CLICK
    overlay.addEventListener("click", () => {
        closeMenu(true);
    });

    // CLOSE WHEN A NAVIGATION LINK IS CLICKED
    navLinks.forEach((link) => {
        link.addEventListener("click", () => {
            closeMenu();

            navLinks.forEach((item) => {
                item.classList.remove("active");
            });

            link.classList.add("active");
        });
    });

    // MOBILE BOOKING LINK
    if (mobileBooking) {
        mobileBooking.addEventListener("click", () => {
            closeMenu();
        });
    }

    // ESCAPE KEY
    document.addEventListener("keydown", (event) => {
        if (
            event.key === "Escape" &&
            navigation.classList.contains("is-open")
        ) {
            closeMenu(true);
        }
    });

    // CLOSE MENU WHEN CLICKING OUTSIDE HEADER
    document.addEventListener("click", (event) => {
        if (
            navigation.classList.contains("is-open") &&
            !header.contains(event.target) &&
            !overlay.contains(event.target)
        ) {
            closeMenu();
        }
    });

    // CLOSE MENU WHEN RESIZING TO DESKTOP
    window.addEventListener("resize", () => {
        if (window.innerWidth > 900) {
            closeMenu();
        }
    });

    // STICKY HEADER SCROLL EFFECT
    let ticking = false;

    function updateHeader() {
        header.classList.toggle("scrolled", window.scrollY > 20);
        ticking = false;
    }

    window.addEventListener("scroll", () => {
        if (!ticking) {
            window.requestAnimationFrame(updateHeader);
            ticking = true;
        }
    }, { passive: true });

    updateHeader();

    // ACTIVE LINK BASED ON PAGE SECTION
    const sections = document.querySelectorAll(
        "#home, #veg-food, #about, #orders, #booking, #contact"
    );

    if ("IntersectionObserver" in window && sections.length > 0) {
        const observer = new IntersectionObserver(
            (entries) => {
                entries.forEach((entry) => {
                    if (!entry.isIntersecting) return;

                    const currentId = entry.target.id;

                    navLinks.forEach((link) => {
                        const isActive =
                            link.getAttribute("href") === `#${currentId}`;

                        link.classList.toggle("active", isActive);
                    });
                });
            },
            {
                rootMargin: "-25% 0px -65% 0px",
                threshold: 0
            }
        );

        sections.forEach((section) => observer.observe(section));
    }
});

// slider function 
document.addEventListener("DOMContentLoaded", function () {
    const slider = document.querySelector(".slider-imges");
    const slides = document.querySelectorAll(".slider-imges .imges");
    const prevBtn = document.querySelector(".arror1");
    const nextBtn = document.querySelector(".arror2");
    const dotsBox = document.querySelector(".slider-dots");
    const current = document.querySelector(".current-slide");
    const total = document.querySelector(".total-slides");
    const box = document.querySelector(".arror-box");

    if (!slider || !slides.length || !prevBtn || !nextBtn || !dotsBox || !box) {
        return;
    }

    let index = 0;
    let timer;
    let touchStart = 0;
    let isPaused = false;

    const count = slides.length;

    const format = n => String(n).padStart(2, "0");

    total.textContent = format(count);

    // Create one dot for each Django slider image
    slides.forEach((slide, i) => {
        const dot = document.createElement("button");

        dot.type = "button";
        dot.className = "slider-dot";
        dot.setAttribute("aria-label", `Show slide ${i + 1}`);

        dot.addEventListener("click", () => {
            showSlide(i);
            restart();
        });

        dotsBox.appendChild(dot);
    });

    const dots = dotsBox.querySelectorAll(".slider-dot");

    function showSlide(nextIndex) {
        index = (nextIndex + count) % count;

        slider.style.transform = `translateX(-${index * 100}%)`;

        slides.forEach((slide, i) => {
            slide.classList.toggle("active", i === index);
        });

        dots.forEach((dot, i) => {
            dot.classList.toggle("active", i === index);

            if (i === index) {
                dot.setAttribute("aria-current", "true");
            } else {
                dot.removeAttribute("aria-current");
            }
        });

        current.textContent = format(index + 1);
    }

    function stop() {
        clearInterval(timer);
    }

    function start() {
        stop();

        if (count > 1 && !isPaused && !document.hidden) {
            timer = setInterval(() => {
                showSlide(index + 1);
            }, 5000);
        }
    }

    function restart() {
        start();
    }

    prevBtn.addEventListener("click", () => {
        showSlide(index - 1);
        restart();
    });

    nextBtn.addEventListener("click", () => {
        showSlide(index + 1);
        restart();
    });

    // Pause autoplay while interacting with the slider
    box.addEventListener("mouseenter", () => {
        isPaused = true;
        stop();
    });

    box.addEventListener("mouseleave", () => {
        isPaused = false;
        start();
    });

    box.addEventListener("focusin", () => {
        isPaused = true;
        stop();
    });

    box.addEventListener("focusout", event => {
        if (!box.contains(event.relatedTarget)) {
            isPaused = false;
            start();
        }
    });

    document.addEventListener("visibilitychange", start);

    // Mobile swipe
    box.addEventListener("touchstart", event => {
        touchStart = event.changedTouches[0].clientX;
    }, { passive: true });

    box.addEventListener("touchend", event => {
        const difference = event.changedTouches[0].clientX - touchStart;

        if (Math.abs(difference) > 50) {
            showSlide(index + (difference < 0 ? 1 : -1));
            restart();
        }
    }, { passive: true });

    showSlide(0);
    start();
});