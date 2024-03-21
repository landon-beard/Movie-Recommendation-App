// dark_mode.js
document.addEventListener('DOMContentLoaded', function () {
    const darkModeToggle = document.getElementById('dark-mode-toggle');
    const body = document.body;

    darkModeToggle.addEventListener('click', function () {
        body.classList.toggle('dark-mode');
        // Save the user's preference to local storage
        const darkModeEnabled = body.classList.contains('dark-mode');
        localStorage.setItem('darkModeEnabled', darkModeEnabled);
    });

    // Check the user's preference from local storage
    const storedDarkMode = localStorage.getItem('darkModeEnabled');
    if (storedDarkMode === 'true') {
        body.classList.add('dark-mode');
    }
});
