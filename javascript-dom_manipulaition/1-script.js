// element.addEventListener("type of event", functionToExecute)

const click = document.getElementById('red_header');

click.addEventListener("click", function () {
    this.style.color = "#FF0000";
});
