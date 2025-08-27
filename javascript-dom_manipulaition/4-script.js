const list = document.querySelector(".my_list");
const add_item = document.getElementById("add_item")

add_item.addEventListener("click", function () {
    const newLi = document.createElement("li");
    newLi.textContent = "Item";
    list.appendChild(newLi);
})
