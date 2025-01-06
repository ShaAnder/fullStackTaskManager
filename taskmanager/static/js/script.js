
const mobileMenuButton = document.getElementById("mobileMenuButton");
const mobileMenu = document.getElementById("mobileMenu");

// Track if the menu is open
let navMenuOpen = false;

// Toggle menu and focus class
mobileMenuButton.addEventListener("click", function () {
    navMenuOpen = !navMenuOpen;
    mobileMenu.style.display = navMenuOpen ? "block" : "none";
});


