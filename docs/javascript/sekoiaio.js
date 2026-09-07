window.addEventListener("DOMContentLoaded", (event) => {
    const ul = document.querySelector('.md-tabs__list');
    ul?.insertAdjacentHTML("beforeend", "<li class='md-tabs__item'><a class='md-tabs__link' href='https://changelog.sekoia.com' target='_blank'>Changelog</a></li>");

    const headerSource = document.querySelector(".md-header__source");

    if (headerSource && !document.querySelector(".sekoia-header-links")) {
        headerSource.insertAdjacentHTML(
            "beforebegin",
            `
            <nav class="sekoia-header-links" aria-label="External links">
                <a
                    class="sekoia-header-link"
                    href="https://www.sekoia.com/blog"
                    target="_blank"
                    rel="noopener"
                >
                    Blog
                </a>
                <a
                    class="sekoia-header-link"
                    href="https://github.com/SEKOIA-IO/Community"
                    target="_blank"
                    rel="noopener"
                >
                    Community
                </a>
                <a
                    class="sekoia-header-link sekoia-header-link--primary"
                    href="https://www.sekoia.com/contact"
                    target="_blank"
                    rel="noopener"
                >
                    Book a demo
                </a>
            </nav>
            `
        );

        headerSource.remove();
    }

    var elements = document.getElementsByClassName("lightgallery");
    for(var i=0; i<elements.length; i++) {
        lightGallery(elements[i]);
    }
});
