grecaptcha.ready(function() {
    grecaptcha.execute('6LeaZHQrAAAAANvtkYEp4PmM8Snsc2kJimiisXph', {action: 'gate'}).then(function(token) {
        document.getElementById('g-recaptcha-response').value = token;
    });
});

(function() {
    const cookieExists = document.cookie.split(";").some(c => c.trim().startsWith("js_enabled="));
    const jsChecked = sessionStorage.getItem("jsChecked");
    if (!cookieExists) {
        document.cookie = "js_enabled=1; path=/";
        if (!jsChecked) {
            sessionStorage.setItem("jsChecked", "true");
            location.reload();
        }
    }
})();