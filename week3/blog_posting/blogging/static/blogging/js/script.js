/* Global JavaScript for the blogging application
 * This file contains all the JavaScript functionality for the blogging site
 */

// Wait for the DOM to be fully loaded before executing the code
document.addEventListener("DOMContentLoaded", function () {

    // Select all elements with the 'fade-in' class
    const fadeInElements = document.querySelectorAll(".fade-in");

    const observer = new IntersectionObserver(
        // Callback function that's executed when visibility changes

        entries => {
            entries.forEach(entry => {

                // If the element becomes visible in the viewport, add 'visible' class to trigger the fade-in animation
                if (entry.isIntersecting) {
                    entry.target.classList.add("visible");
                    // Stop observing the element after it's been revealed
                    observer.unobserve(entry.target);
                }
            });
        },
        // Options object: threshold of 0.1 means the callback will be executed 
        // when at least 10% of the target element is visible
        { threshold: 0.1 }
    );

    // Start observing each fade-in element
    fadeInElements.forEach(el => {
        observer.observe(el);
    });
});