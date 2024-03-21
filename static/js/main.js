document.addEventListener('DOMContentLoaded', (event) => {
    console.log("The DOM has fully loaded.");
    // Example of event listener for form submission
    document.querySelector('form').addEventListener('submit', () => {
        console.log("Form submitted.");
        // You could add more interactive elements here, like form validation or dynamic content loading
    });
});
