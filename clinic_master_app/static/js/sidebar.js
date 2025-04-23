document.addEventListener("DOMContentLoaded", function () {
    const menuBtn = document.querySelector('.menu-btn');
    const sidebar = document.getElementById('sidebarMenu');
    menuBtn.addEventListener('click', function () {
        sidebar.classList.toggle('show');
        document.body.classList.toggle('sidebar-visible');
    });
});
