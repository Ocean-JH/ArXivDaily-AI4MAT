// Dark Mode Toggle
const toggleButton = document.getElementById('theme-toggle');
toggleButton.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    if (document.body.classList.contains('dark-mode')) {
        toggleButton.textContent = '☀️ Day';
    } else {
        toggleButton.textContent = '🌙 Night';
    }
});