const activation = document.getElementById('activate');
activation.addEventListener('click', () => {
    const activated = true;
    toggleBackground(activated);
})
function toggleBackground(status) {
    const canvasSection = document.getElementById("interface");
    const premiumSection = document.getElementById("premium");
    const titleHeader = document.getElementById("title");
    const clientTitleHeader = document.getElementById("clientTitle");
    const statusHeader = document.getElementById("status");
    const statusClient = document.getElementById("clientStatus");
    const descText = document.getElementById("desc");
    const passButton = document.getElementById("pass");
    const activateButton = document.getElementById("activate");
    const textInput = document.getElementById("text");
    const typeInput = document.getElementById("type");
    const dragdropInput = document.getElementById("dragdrop");
    const timeInput = document.getElementById("time");
    const trapsInput = document.getElementById("traps");
    const affected = [canvasSection, premiumSection];
    const flashing = [titleHeader, clientTitleHeader, statusHeader, statusClient, descText, passButton];
    const changing = [passButton, textInput, typeInput, dragdropInput, timeInput, trapsInput]
    if (status) {
        passButton.classList.add("upgraded");
        activateButton.classList.add("upgraded");
        setTimeout(() => {
            affected.forEach((aff) => { aff.classList.add("upgraded"); });
            flashing.forEach((fla) => { fla.classList.add("flash"); });
            setTimeout(() => {
                flashing.forEach((fla) => { fla.classList.add("upgraded"); });
                changing.forEach((cha) => { cha.classList.add("upgradedFont"); });
                statusHeader.textContent = "Premium";
                statusClient.textContent = "Premium";
                descText.innerHTML = "Correctly using GPT<br>for your GPA";
            }, 2000)
        }, 1000)
    }
}