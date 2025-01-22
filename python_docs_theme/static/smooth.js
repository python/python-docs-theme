window.addEventListener('load', function() {
    document.documentElement.style.scrollBehavior = 'auto';

    const target = window.location.hash;
    if (target) {
        window.scrollTo(0, 0);
        document.querySelector(target)?.scrollIntoView();
    }

    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            document.documentElement.style.scrollBehavior = 'smooth';
        });
    });
});
