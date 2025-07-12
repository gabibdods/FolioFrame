const dragdrop = document.getElementById('dragdrop');
const input = document.getElementById('input');
const explore = document.getElementById('explore');
explore.addEventListener('click', () => input.click());
dragdrop.addEventListener('dragover', (e) => {
    e.preventDefault();
    dragdrop.classList.add('dragover');
});
dragdrop.addEventListener('dragleave', () => {
    dragdrop.classList.remove('dragover');
});
dragdrop.addEventListener('drop', (e) => {
    e.preventDefault();
    dragdrop.classList.remove('dragover');
    const files = e.dataTransfer.files;
    handleFiles(files);
});
input.addEventListener('change', () => {
    handleFiles(input.files);
});
function handleFiles(files) {                   //change this ofc
    for (const file of files) {
        console.log(file.name);
    }
}

const textArea = document.getElementById('text');
const type = document.getElementById('type');
const time = document.getElementById('time');
const traps = document.getElementById('traps');
function repositionFields() {
    const baseTop = textArea.scrollHeight + 20;
    type.style.top = `${baseTop}px`;
    dragdrop.style.top = `${baseTop}px`;
    time.style.top = `${baseTop + 70}px`;
    traps.style.top = `${baseTop + 70}px`;
}
repositionFields();
const client = document.getElementById('client');
textArea.addEventListener('input', () => {
    textArea.style.height = 'auto';
    textArea.style.height = textArea.scrollHeight + 'px';
    repositionFields();
    const lineHeight = parseFloat(getComputedStyle(textArea).lineHeight || 24);
    const lines = Math.floor(textArea.scrollHeight / lineHeight);
    let newPadding = 0;
    if (lines >= 1){
        newPadding = 1 + (lines - 1) * 3;
    }
    client.style.paddingBottom = `${newPadding * 16 + 248}px`;
});

let passed = 0;
function scalePage() {
    const scaleX = window.innerWidth / 1920;
    const scaleY = window.innerHeight / 1080;
    const scale = Math.min(scaleX, scaleY);
    document.querySelector('#top').style.transform = `scale(${scale})`;
    document.querySelector('#bottom').style.transform = `scale(${scale})`;
    document.querySelector('#tank').style.transform = `scale(${scale * 3})`;
    if (passed === 1){
        const dest = document.querySelector('#client');
        if (dest) {
            dest.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
    }
}
window.addEventListener('resize', scalePage);
window.addEventListener('load', scalePage);

document.querySelector('#pass').addEventListener('click', (e) => {
    e.preventDefault();
    passed = 1;
    document.querySelector('#client').scrollIntoView({ behavior: 'smooth', block: 'center' });
});