document.addEventListener("DOMContentLoaded", () => {
    const activate = document.getElementById("activate");
    const standard = document.getElementById("standard");
    const premium = document.getElementById("premium");
    const clientMessage = document.getElementById("clientMessage");
    const dragdropPlaceholder = document.getElementById("dragdropPlaceholder");
    const input = document.getElementById("input");
    const answer = document.getElementById("answer");
    const answerMessage = document.getElementById("answerMessage");

    clientMessage.addEventListener("submit", async function (event) {
        event.preventDefault();

        const formData = new FormData();
        const fileInput = document.getElementById("input");
        formData.append("file", fileInput.files[0]);

        const response = await fetch("http://127.0.0.1:8081/parse/", {
            method: "POST",
            body: formData
        });
        const result = await response.json();
        answerMessage.textContent = JSON.stringify(result, null, 2);

        answer.scrollIntoView({ behavior: "smooth", block: "center" });
    });
    input.addEventListener("change", (e) => {
        const file = e.target.files[0];
        if (file) {
            dragdropPlaceholder.textContent = file.name;
        } else {
            dragdropPlaceholder.textContent = "Any presets?";
        }
    });
    activate.addEventListener("click", () => {
        standard.style.opacity = "0";
        premium.style.opacity = "1";
    });
});