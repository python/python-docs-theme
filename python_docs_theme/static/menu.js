
document.addEventListener('DOMContentLoaded', function () {
    const toggler = document.querySelector('.toggler');
    const sideMenu = document.querySelector('.menu-wrapper');
    const doc = document.querySelector('.document');

    function closeMenu() {
        sideMenu.classList.remove('open');
        toggler.classList.remove('active');
        toggler.setAttribute("aria-expanded", 'false');
    }
    function isMenuOpen(){
        return (' ' + sideMenu.className + ' ').indexOf(' open ') > -1;
    }

    sideMenu.addEventListener('click', function (event) {
        // Close menu only if a link on the sideMenu is clicked
        let target = event.target;
        if (target.tagName !== 'a') return;
        closeMenu();
    })
    toggler.addEventListener('click', function (e) {
        if (!isMenuOpen()) {
            sideMenu.classList.add('open');
            toggler.classList.add('active');
            toggler.setAttribute("aria-expanded", 'true');
        } else {
            closeMenu();
        }
    });
    doc.addEventListener('click', function () {
        if (isMenuOpen()) {
            closeMenu();
        }
    })
})