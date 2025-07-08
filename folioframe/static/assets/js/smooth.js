document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a[smooth-scroll-menu]').forEach(function(a) {
        a.addEventListener('click', function (e) {
            e.preventDefault();
            const id = this.hash.substring(1);
            const section = document.getElementById(id);
            if (section) {
                section.scrollIntoView({ behavior: 'smooth' });
            } else {
                window.location.href = this.href;
            }
        });
    });
});