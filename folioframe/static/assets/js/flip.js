window.addEventListener('DOMContentLoaded', themeByTime);
setInterval(themeByTime, 2*10*60*1000);
function themeByTime () {
    const h = new Date().getHours();
    if (6 <= h && h < 21) {
        document.body.style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("theme-switcher-grid").classList.remove("night-theme");
    } else {
        document.body.style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("theme-switcher-grid").classList.add("night-theme");
    }
}
document.getElementById("theme-switcher-grid").addEventListener("click", function () {
    this.classList.toggle("night-theme");
    document.body.style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("navbar").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
});