document.addEventListener('DOMContentLoaded', function () {
    let openMenuBtn = document.getElementById('openMenu');
    let closeMenuBtn = document.getElementById('closeMenu');
    let menu = document.getElementById('menuContent');

    openMenuBtn.addEventListener('click', function () {
        menu.classList.toggle('hidden');
    });
    closeMenuBtn.addEventListener('click', function () {
        menu.classList.toggle('hidden');
    });
});