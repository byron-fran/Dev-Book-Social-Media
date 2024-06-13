document.addEventListener('DOMContentLoaded', () => {

    const menuButton = document.querySelector('#menu');
    const sidebar = document.querySelector('#sidebar');
    const body = document.body;

    const hideSidebar = () => {
        sidebar.classList.remove('flex', 'absolute', 'h-screen', 'z-50', 'bg-white', 'top-0', 'w-[80%]');
        sidebar.classList.add('hidden');
        body.classList.remove('sidebar-open');
    };

    menuButton.addEventListener('click', (e) => {

        e.stopPropagation();
        sidebar.classList.add('flex', 'absolute', 'h-screen', 'z-50', 'bg-white', 'top-0', 'w-[80%]');
        sidebar.classList.remove('hidden');
        body.classList.add('sidebar-open');

    });

    window.addEventListener('click', (e) => {
        if (!sidebar.contains(e.target) && !menuButton.contains(e.target)) {
            hideSidebar();
        }
    });

    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768) {
            hideSidebar();
        }
    });
});
