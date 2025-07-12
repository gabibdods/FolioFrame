window.addEventListener('DOMContentLoaded', themeByTime);
setInterval(themeByTime, 20*60*1000);
const overlays = document.getElementsByClassName("isotope-overlay");
const overlaysLength = document.getElementsByClassName("isotope-overlay").length;

function themeByTime () {
    const h = new Date().getHours();
    if (h <= 1 || 10 <= h) {
        document.body.style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-light)";
        for(let i = 0; i < overlaysLength; i++) { overlays[i].style.background = "var(--bg-color-light-start-overlay)"; }
        document.querySelector(".welcome-hero").classList.remove("night-theme");
        document.getElementById("theme-switcher-grid").classList.remove("night-theme");
    } else {
        document.body.style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-dark)";
        for(let i = 0; i < overlaysLength; i++) { overlays[i].style.background = "var(--bg-color-light-start-overlay)"; }
        document.querySelector(".welcome-hero").classList.add("night-theme");
        document.getElementById("theme-switcher-grid").classList.add("night-theme");
    }
}
document.getElementById("theme-switcher-grid").addEventListener("click", function () {
    this.classList.toggle("night-theme");
    document.body.style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("navbar").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    for(let i = 0; i < overlaysLength; i++) { overlays[i].style.background = this.classList.contains("night-theme") ? "var(--bg-color-before-clear)" : "var(--bg-color-light-start-overlay)"; }
    document.querySelector(".welcome-hero").classList.toggle("night-theme");
});