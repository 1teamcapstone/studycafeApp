const menuButton = document.querySelector('#menu-button');
const menuContainer = document.querySelector('.menu-container');
const closeButton = document.querySelector('.close-button');

menuButton.addEventListener('click', () => {
  menuContainer.style.transform = 'translateX(0)';
});

closeButton.addEventListener('click', () => {
  menuContainer.style.transform = 'translateX(-100%)';
});