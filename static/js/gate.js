document.addEventListener("DOMContentLoaded", () => {
    const btn = document.getElementById("enable-js-btn");
    if (btn) btn.addEventListener("click", () => {
        const cookieName = "js_enabled";
        const cookieExists = document.cookie.split(";").some(c => c.trim().startsWith(cookieName + "="));
        const jsChecked = sessionStorage.getItem("jsChecked");

        if (!cookieExists) {
            document.cookie = cookieName + "=1; path=/";
            if (!jsChecked) {
                sessionStorage.setItem("jsChecked", "true");
                location.reload();
            }
        }
        if (cookieExists) {
	    cookieValue = document.cookie.match(new RegExp('(?:^|; )' + cookieName.replace(/[-[\]{}()*+?.,\\^$|#\s]/g, '\\$&') + '=([^;]*)'))
            const val = cookieValue ? decodeURIComponent(cookieValue[1]) : null;
            if (val === "1") {
                window.location.assign("/ff/home/");
            } else {
                window.location.assign("/ff/428/");
            }
        }
    });
});
