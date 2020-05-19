
document.addEventListener('DOMContentLoaded', function () {
    const toggler = document.querySelector('.toggler');
    const sideMenu = document.querySelector('.menu-wrapper');
    const doc = document.querySelector('.document');
    function closeMenu() {
        sideMenu.classList.remove('open');
        toggler.checked = false;
    }
    toggler.addEventListener('change', function (e) {
        if (toggler.checked) {
            sideMenu.classList.add('open');
        } else {
            closeMenu();
        }
    });
    doc.addEventListener('click', function () {
        if (toggler.checked) {
            closeMenu();
        }
    })
})