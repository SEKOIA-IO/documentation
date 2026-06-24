window.addEventListener("DOMContentLoaded", (event) => {
    const ul = document.querySelector('.md-tabs__list');
    ul?.insertAdjacentHTML("beforeend", "<li class='md-tabs__item'><a class='md-tabs__link' href='https://changelog.sekoia.com' target='_blank'>Changelog</a></li>");

    var elements = document.getElementsByClassName("lightgallery");
    for(var i=0; i<elements.length; i++) {
        lightGallery(elements[i]);
    }
});

(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],j=d.createElement(s);j.async=true;j.src="https://ksxk.sekoia.com/4j0bfgtunkswv.js?"+i;f.parentNode.insertBefore(j,f);})(window,document,'script','dataLayer','bvoy7=HxNOLDo4WSk1OUBcP0BSEUtFXVpIERpaBRIYBAcUWgQZGg%3D%3D');
