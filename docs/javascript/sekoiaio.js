window.addEventListener("DOMContentLoaded", (event) => {
    var divs = document.querySelectorAll('h2');

    [].forEach.call(divs, function(div) {
        let p = document.createElement("span");
        div.prepend(p);
    });

    var uls = document.getElementsByClassName("md-tabs__list");
    if (uls.length != 0) {
	uls[0].insertAdjacentHTML("beforeend", "<li class='md-tabs__item'><a data-sleek data-badge-changelog class='md-tabs__link' href='#'>Changelog</a></li>");
    }

    window.$sleek=[];window.SLEEK_PRODUCT_ID=901462981;(function(){d=document;s=d.createElement("script");s.src="https://client.sleekplan.com/sdk/e.js";s.async=1;d.getElementsByTagName("head")[0].appendChild(s);})();
});
