window.addEventListener("DOMContentLoaded", (event) => {
    const ul = document.querySelector('.md-tabs__list');
    ul?.insertAdjacentHTML("beforeend", "<li class='md-tabs__item'><a class='md-tabs__link' href='https://changelog.sekoia.io' target='_blank'>Changelog</a></li>");

    var elements = document.getElementsByClassName("lightgallery");
    for(var i=0; i<elements.length; i++) {
        lightGallery(elements[i]);
    }
});
