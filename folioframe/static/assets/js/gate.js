grecaptcha.ready(function() {
    grecaptcha.execute('6LeaZHQrAAAAANvtkYEp4PmM8Snsc2kJimiisXph', {action: 'gate'}).then(function(token) {
        document.getElementById('g-recaptcha-response').value = token;
    });
});