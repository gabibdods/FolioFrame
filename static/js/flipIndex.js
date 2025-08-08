const isotopeOverlays = document.getElementsByClassName("isotope-overlay");
const overlaysLength = document.getElementsByClassName("isotope-overlay").length;
window.addEventListener('DOMContentLoaded', () => {
    const checkbox = document.getElementById("theme-switch");

    indexThemeByTime();

    checkbox.addEventListener("change", () => {
        indexApplyTheme(checkbox.checked);
        localStorage.setItem("themeOverride", checkbox.checked ? "night" : "day");
    });
});
function indexApplyTheme(isNight) {
    document.getElementById("venn-container").style.backgroundImage =
        isNight ? "radial-gradient(#43485c40 45%, transparent 55%)" : "radial-gradient(#fff 45%, transparent 55%)";

    document.getElementById("venn-circle1").style.backgroundColor = isNight ? "rgba(255, 255, 0, 0.7)" : "rgba(0, 255, 255, 0.5)";
    document.getElementById("venn-circle2").style.backgroundColor = isNight ? "rgba(255, 0, 255, 0.7)" : "rgba(255, 0, 255, 0.5)";
    document.getElementById("venn-circle3").style.backgroundColor = isNight ? "rgba(0, 255, 255, 0.7)" : "rgba(255, 255, 0, 0.5)";

    for(let i = 0; i < overlaysLength; i++) {
        isotopeOverlays[i].style.backgroundColor = isNight ? "var(--bg-color-before-clear)" : "var(--bg-color-light-start-overlay)";
    }
}
function indexThemeByTime() {
    const checkbox = document.getElementById("theme-switch");

    const h = new Date().getHours();
    const isNight = h < 8 || h >= 21;
    checkbox.checked = isNight;
    indexApplyTheme(isNight);
}