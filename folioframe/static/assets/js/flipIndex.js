window.addEventListener('DOMContentLoaded', themeByTime);
setInterval(themeByTime, 20*60*1000);
const isotoOverlays = document.getElementsByClassName("isotope-overlay");
const overlaysLength = document.getElementsByClassName("isotope-overlay").length;

function themeByTime () {
    const h = new Date().getHours();
    if (h <= 1 || 10 <= h) {
        document.body.style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("venn-container").style.backgroundImage = "radial-gradient(#fff 45%, transparent 55%)";
        document.getElementById("venn-circle1").style.mixBlendMode = "multiply";
        document.getElementById("venn-circle1").style.backgroundColor = "rgba(0, 255, 255, 0.5)";
        document.getElementById("venn-circle2").style.mixBlendMode = "multiply";
        document.getElementById("venn-circle2").style.backgroundColor = "rgba(255, 0, 255, 0.5)";
        document.getElementById("venn-circle3").style.mixBlendMode = "multiply";
        document.getElementById("venn-circle3").style.backgroundColor = "rgba(255, 255, 0, 0.5)";
        for(let i = 0; i < overlaysLength; i++) { isotoOverlays[i].style.backgroundColor = "var(--bg-color-light-start-overlay)"; }
        document.querySelector(".welcome-hero").classList.remove("night-theme");
        document.getElementById("welcome-header").style.color = "color: var(--txt-color-darker);";
        document.getElementById("welcome-desc").style.color = "color: var(--txt-color-darker);";
        document.getElementById("theme-switcher-grid").classList.remove("night-theme");
    } else {
        document.body.style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("venn-container").style.backgroundImage = "radial-gradient(#43485c40 45%, transparent 55%)";
        document.getElementById("venn-circle1").style.mixBlendMode = "overlay";
        document.getElementById("venn-circle1").style.backgroundColor = "rgba(255, 255, 0, 0.7)";
        document.getElementById("venn-circle2").style.mixBlendMode = "overlay";
        document.getElementById("venn-circle2").style.backgroundColor = "rgba(255, 0, 255, 0.7)";
        document.getElementById("venn-circle3").style.mixBlendMode = "overlay";
        document.getElementById("venn-circle3").style.backgroundColor = "rgba(0, 255, 255, 0.7)";
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
    document.getElementById("venn-container").style.backgroundImage = this.classList.contains("night-theme") ? "radial-gradient(#43485c40 45%, transparent 55%)" : "radial-gradient(#fff 45%, transparent 55%)";
    document.getElementById("venn-circle1").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
    document.getElementById("venn-circle1").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(255, 255, 0, 0.7)" : "rgba(0, 255, 255, 0.5)";
    document.getElementById("venn-circle2").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
    document.getElementById("venn-circle2").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(255, 0, 255, 0.7)" : "rgba(255, 0, 255, 0.5)";
    document.getElementById("venn-circle3").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
    document.getElementById("venn-circle3").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(0, 255, 255, 0.7)" : "rgba(255, 255, 0, 0.5)";
    for(let i = 0; i < overlaysLength; i++) { isotoOverlays[i].style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-before-clear)" : "var(--bg-color-light-start-overlay)"; }
    document.querySelector("#welcome-header").classList.toggle("night-theme");
    document.querySelector("#welcome-desc").classList.toggle("night-theme");
    document.querySelector(".welcome-hero").classList.toggle("night-theme");
});