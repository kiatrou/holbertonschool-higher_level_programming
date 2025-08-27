document.addEventListener('DOMContentLoaded', function() {
    const hello = document.getElementById("hello");
    
    fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
        .then(function(response) {
            return response.json();
        })
        .then(function(data) {
            hello.textContent = data.hello;
        });
});