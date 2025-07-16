function scalePage() {
    const scaleX = window.innerWidth / 1920;
    const scaleY = window.innerHeight / 1080;
    const scale = Math.min(scaleX, scaleY);
    document.querySelector('.scaler').style.transform = `scale(${scale})`;
}
window.addEventListener('resize', scalePage);
window.addEventListener('load', scalePage);