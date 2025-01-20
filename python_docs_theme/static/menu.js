document.addEventListener("DOMContentLoaded", function () {
    // Make tables responsive
    document.querySelectorAll("table.docutils").forEach((table) => {
        table.outerHTML = `<div class="responsive-table__container">${table.outerHTML}</div>`;
    });

    const togglerInput = document.querySelector(".toggler__input");
    const togglerLabel = document.querySelector(".toggler__label");
    const sideMenu = document.querySelector(".menu-wrapper");
    const body = document.body;

    const closeMenu = () => {
        togglerInput.checked = false;
        sideMenu.setAttribute("aria-expanded", "false");
        sideMenu.setAttribute("aria-hidden", "true");
        togglerLabel.setAttribute("aria-pressed", "false");
        body.style.overflow = "visible";
    };

    const openMenu = () => {
        togglerInput.checked = true;
        sideMenu.setAttribute("aria-expanded", "true");
        sideMenu.setAttribute("aria-hidden", "false");
        togglerLabel.setAttribute("aria-pressed", "true");
        body.style.overflow = "hidden";
    };

    // Toggle menu accessibility attributes
    togglerInput.addEventListener("change", () => {
        togglerInput.checked ? openMenu() : closeMenu();
        sideMenu.querySelectorAll(".menu").forEach((menuItem) => {
            menuItem.setAttribute("tabindex", togglerInput.checked ? "0" : "-1");
        });
    });

    // Close menu when a link inside the sideMenu is clicked
    sideMenu.addEventListener("click", (event) => {
        if (event.target.closest("a")) closeMenu();
    });

    // Close menu when the document body is clicked
    document.querySelector(".document").addEventListener("click", () => {
        if (togglerInput.checked) closeMenu();
    });
});
