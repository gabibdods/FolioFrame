const version = "{{ version }}"
const cookieVersion = document.cookie.replace(/(?:^|.*;\s*)app_version\s*=\s*([^;]*).*$|^.*$/, "$1");

if (cookieVersion !== version) {
    document.cookie = "app_version=" + version + ";path=/";
    location.reload();
}