function scalePage() {
    const scaleX = window.innerWidth / 1920;  // Use your design width
    const scaleY = window.innerHeight / 1080; // Use your design height
    const scale = Math.min(scaleX, scaleY);
    document.querySelector('.scaler').style.transform = `scale(${scale})`;
  }

  window.addEventListener('resize', scalePage);
  window.addEventListener('load', scalePage);

document.cookie = "js_enabled=1; path=/";