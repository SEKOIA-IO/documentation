window.addEventListener("DOMContentLoaded", (event) => {
    var divs = document.querySelectorAll('h2');

    [].forEach.call(divs, function(div) {
        let p = document.createElement("span");
        div.prepend(p);
    });
});
