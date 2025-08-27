const header = document.querySelector("header");
const toggle_header = document.getElementById("toggle_header")

toggle_header.addEventListener("click", function () {
    if (header.classList.contains("green")) {
        header.classList.remove("green");
        header.classList.add("red");
    } else {
        header.classList.remove("red");
        header.classList.add("green");
    }
});
