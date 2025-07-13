window.addEventListener('DOMContentLoaded', () => {
    const checkbox = document.getElementById("theme-switch");

    themeByTime();

    checkbox.addEventListener("change", () => {
        applyTheme(checkbox.checked);
        localStorage.setItem("themeOverride", checkbox.checked ? "night" : "day");
    });
});
function applyTheme(isNight) {
    const bgColor = isNight ? "var(--bg-color-dark)" : "var(--bg-color-light)";

    document.body.style.backgroundColor = bgColor;

    document.getElementById("navbar")?.style.setProperty("background-color", bgColor);
    document.getElementById("welcome-hero")?.classList.toggle("night-theme", isNight);
    document.getElementById("welcome-header")?.classList.toggle("night-theme", isNight);
    document.getElementById("welcome-desc")?.classList.toggle("night-theme", isNight);
}
function themeByTime() {
    const checkbox = document.getElementById("theme-switch");

    const h = new Date().getHours();
    const isNight = h < 8 || h >= 21;
    checkbox.checked = isNight;
    applyTheme(isNight);
}