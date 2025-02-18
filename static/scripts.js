document.addEventListener("DOMContentLoaded", function() {
    const alertBoxes = document.querySelectorAll(".alert");
    alertBoxes.forEach(alert => {
        setTimeout(() => {
            alert.style.display = "none";
        }, 5000);
    });

    const buttons = document.querySelectorAll("button");
    buttons.forEach(button => {
        button.addEventListener("click", function() {
            alert("Button clicked: " + this.innerText);
        });
    });
});
