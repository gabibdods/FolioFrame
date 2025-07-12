window.addEventListener('DOMContentLoaded', themeByTime);
setInterval(themeByTime, 20*60*1000);
const isotoOverlays = document.getElementsByClassName("isotope-overlay");
const overlaysLength = document.getElementsByClassName("isotope-overlay").length;

function themeByTime () {
    const h = new Date().getHours();
    if (h <= 1 || 10 <= h) {
        document.body.style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-light)";
        for(let i = 0; i < overlaysLength; i++) { isotoOverlays[i].style.backgroundColor = "var(--bg-color-light-start-overlay)"; }
        document.querySelector(".welcome-hero").classList.remove("night-theme");
        document.getElementById("welcome-header").style.color = "color: var(--txt-color-darker);";
        document.getElementById("welcome-desc").style.color = "color: var(--txt-color-darker);";
        document.getElementById("theme-switcher-grid").classList.remove("night-theme");
    } else {
        document.body.style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-dark)";
        for(let i = 0; i < overlaysLength; i++) { isotoOverlays[i].style.backgroundColor = "var(--bg-color-light-start-overlay)"; }
        document.querySelector(".welcome-hero").classList.add("night-theme");
        document.getElementById("welcome-header").style.color = "#fff";
        document.getElementById("welcome-desc").style.color = "#fff";
        document.getElementById("theme-switcher-grid").classList.add("night-theme");
    }
}
document.getElementById("theme-switcher-grid").addEventListener("click", function () {
    this.classList.toggle("night-theme");
    document.body.style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("navbar").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    for(let i = 0; i < overlaysLength; i++) { isotoOverlays[i].style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-before-clear)" : "var(--bg-color-light-start-overlay)"; }
    document.querySelector("#welcome-header").classList.toggle("night-theme");
    document.querySelector("#welcome-desc").classList.toggle("night-theme");
    document.querySelector(".welcome-hero").classList.toggle("night-theme");
});