document.getElementById('get-started-btn').addEventListener('click', function(e) {
    e.preventDefault();  // Prevent default link behavior
    // Add the swoosh-out class to the container or main section
    document.querySelector('body').classList.add('swoosh-out');

    // Wait for the animation to finish, then redirect to the second page
    setTimeout(function() {
        window.location.href = '/getstarted'; //Your Second Page URL here
    }, 1000);  // Match this time with your animation duration
});
