const header = document.querySelector("header");
const update_header = document.getElementById("update_header");

update_header.addEventListener("click", function () {
    header.textContent = "New Header!!!";
})
