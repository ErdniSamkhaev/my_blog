document.addEventListener("DOMContentLoaded", function() {
    document.querySelector('.toggle-password').addEventListener('click', function() {
        const input = document.querySelector(this.getAttribute('toggle'));
        if (input.type === "password") {
            input.type = "text";
        } else {
            input.type = "password";
        }
    });
});
