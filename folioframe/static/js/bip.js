document.getElementById("bip-form").addEventListener("submit", async function(event) {
    event.preventDefault();
    console.log("submitted");
    const formData = new FormData();
    const fileInput = document.getElementById("input");
    formData.append("file", fileInput.files[0]);
    console.log("appended");
    const response = await fetch("http://localhost:8081/parse/", {
        method: "POST",
        body: formData
    });
    const result = await response.json();
    document.getElementById("text").textContent = JSON.stringify(result, null, 2);
    console.log("resulted");
});