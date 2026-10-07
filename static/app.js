// ===============================
// FLOWER HOME PAGE
// ===============================


// ===============================
// 1. CART SIDEBAR
// ===============================

const btn = document.getElementById("cart-add");
const sidebar = document.getElementById("sidebar");

let cartOpen = false;

if (btn && sidebar) {
    btn.addEventListener("click", function () {

        if (!cartOpen) {
            sidebar.style.transform = "translateX(0)";
            cartOpen = true;
        } else {
            sidebar.style.transform = "translateX(100%)";
            cartOpen = false;
        }

    });
}


// ===============================
// 2. MOBILE MENU
// ===============================

const menuButton = document.getElementById("manue1");
const nav = document.getElementById("navbtn");
const closeButton = document.getElementById("x");
const loginButtons = document.querySelectorAll(".login");

if (menuButton && nav) {

    menuButton.addEventListener("click", function () {

        nav.style.display = "grid";
        nav.style.backgroundColor = "#666";
        nav.style.position = "absolute";
        nav.style.top = "60px";
        nav.style.right = "0";
        nav.style.width = "70%";
        nav.style.padding = "10px";
        nav.style.zIndex = "999";

        if (closeButton) {
            closeButton.style.display = "block";
        }

    });

}


// ===============================
// 3. CLOSE MOBILE MENU
// ===============================

if (closeButton && nav) {

    closeButton.addEventListener("click", function () {

        nav.style.display = "none";
        closeButton.style.display = "none";

    });

}