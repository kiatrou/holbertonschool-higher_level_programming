const header = document.querySelector("header");
const redHeaderButton = document.getElementById("red_header");

redHeaderButton.addEventListener("click", function () {
    header.classList.add("red");
});
