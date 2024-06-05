document.addEventListener('DOMContentLoaded', () => {
    
    const menuButton = document.querySelector('#menu')
    const sidebar = document.querySelector('#sidebar')
    const body = document.body

    const hideSidebar = () => {

        sidebar.classList.remove('flex', 'absolute', 'h-screen', 'z-50',  'top-0', 'w-[80%]', 'transition-all', 'ease-in-out');
        sidebar.classList.add('hidden', 'w-full');
       // body.classList.remove('sidebar-open');

    };

    menuButton.addEventListener('click', (e) => {

        e.stopPropagation()
        sidebar.classList.add('flex', 'absolute', 'h-screen', 'z-50', 'bg-white', 'top-0', 'w-[80%]', 'transition-all', 'ease-in-out');
        sidebar.classList.remove('hidden', 'w-full');

    })

    window.addEventListener('click', (e) => {

        if (!sidebar.contains(e.target) && !menuButton.contains(e.target)) {
            sidebar.classList.remove('flex', 'absolute', 'h-screen', 'z-50', 'bg-white', 'top-0', 'w-[80%]', 'transition-all', 'ease-in-out');
            sidebar.classList.add('hidden','w-full');
          
        } 
    });
    window.addEventListener('resize', () => {
        if (window.innerWidth >= 768) {
            hideSidebar();
            return
        }
        sidebar.classList.add('w-[80%]');
    });
})