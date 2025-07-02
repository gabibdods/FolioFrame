window.addEventListener('DOMContentLoaded', themeByTime);
setInterval(themeByTime, 2*10*60*1000);
function themeByTime () {
    const h = new Date().getHours();
    if (6 <= h && h < 21) {
        document.body.style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("name").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("email").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("subject").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("message").style.backgroundColor = "var(--bg-color-light)";
        document.getElementById("venn-container").style.backgroundImage = "radial-gradient(#fff 45%, transparent 55%)";
        document.getElementById("venn-circle1").style.backgroundColor = "rgba(0, 255, 255, 0.5)";
        document.getElementById("venn-circle2").style.backgroundColor = "rgba(255, 0, 255, 0.5)";
        document.getElementById("venn-circle3").style.backgroundColor = "rgba(255, 255, 0, 0.5)";
        document.getElementById("venn-circle1").style.mixBlendMode = "multiply";
        document.getElementById("venn-circle2").style.mixBlendMode = "multiply";
        document.getElementById("venn-circle3").style.mixBlendMode = "multiply";
        document.getElementById("theme-switcher-grid").classList.remove("night-theme");
    } else {
        document.body.style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("navbar").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("name").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("email").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("subject").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("message").style.backgroundColor = "var(--bg-color-dark)";
        document.getElementById("venn-container").style.backgroundImage = "radial-gradient(#43485c40 45%, transparent 55%)";
        document.getElementById("venn-circle1").style.backgroundColor = "rgba(255, 255, 0, 0.7)";
        document.getElementById("venn-circle2").style.backgroundColor = "rgba(255, 0, 255, 0.7)";
        document.getElementById("venn-circle3").style.backgroundColor = "rgba(0, 255, 255, 0.7)";
        document.getElementById("venn-circle1").style.mixBlendMode = "overlay";
        document.getElementById("venn-circle2").style.mixBlendMode = "overlay";
        document.getElementById("venn-circle3").style.mixBlendMode = "overlay";
        document.getElementById("theme-switcher-grid").classList.add("night-theme");
    }
}
document.getElementById("theme-switcher-grid").addEventListener("click", function () {
    this.classList.toggle("night-theme");
    document.body.style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("navbar").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("name").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("email").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("subject").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("message").style.backgroundColor = this.classList.contains("night-theme") ? "var(--bg-color-dark)" : "var(--bg-color-light)";
    document.getElementById("venn-container").style.backgroundImage = this.classList.contains("night-theme") ? "radial-gradient(#43485c40 45%, transparent 55%)" : "radial-gradient(#fff 45%, transparent 55%)";
    document.getElementById("venn-circle1").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(255, 255, 0, 0.7)" : "rgba(0, 255, 255, 0.5)";
    document.getElementById("venn-circle2").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(255, 0, 255, 0.7)" : "rgba(255, 0, 255, 0.5)";
    document.getElementById("venn-circle3").style.backgroundColor = this.classList.contains("night-theme") ? "rgba(0, 255, 255, 0.7)" : "rgba(255, 255, 0, 0.5)";
    document.getElementById("venn-circle1").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
    document.getElementById("venn-circle2").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
    document.getElementById("venn-circle3").style.mixBlendMode = this.classList.contains("night-theme") ? "overlay" : "multiply";
});