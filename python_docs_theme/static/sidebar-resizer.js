document.addEventListener('DOMContentLoaded', function() {
    const sidebar = document.querySelector('.sphinxsidebar');
    const resizer = document.createElement('div');
    resizer.className = 'sidebar-resizer';
    sidebar.appendChild(resizer);

    resizer.addEventListener('mousedown', function(e) {
        document.addEventListener('mousemove', resizeSidebar);
        document.addEventListener('mouseup', stopResize);
    });

    function resizeSidebar(e) {
        const newWidth = e.clientX - sidebar.getBoundingClientRect().left;
        if (newWidth > 150 && newWidth < window.innerWidth - 100) {
            sidebar.style.width = newWidth + 'px';
        }
    }

    function stopResize() {
        document.removeEventListener('mousemove', resizeSidebar);
        document.removeEventListener('mouseup', stopResize);
    }
});
