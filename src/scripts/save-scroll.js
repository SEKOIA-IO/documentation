document.addEventListener("DOMContentLoaded", function () {
    var derniere_position_de_scroll_connue = 0;
    var ticking = false;
    var currentLocation = window.location.pathname;

    if (localStorage.getItem(currentLocation) != null) {
        window.scrollTo({
            top: localStorage.getItem(currentLocation),
            left: 0,
        });
    }

    window.addEventListener("scroll", function (e) {
        derniere_position_de_scroll_connue = window.scrollY;
        console.log(derniere_position_de_scroll_connue);

        if (!ticking) {
            window.requestAnimationFrame(function () {
                localStorage.setItem(
                    currentLocation,
                    derniere_position_de_scroll_connue
                );
                ticking = false;
            });
        }

        ticking = true;
    });

    !function(d,w){var t="SnAXhNw0z8weNqK5AkDkp3pNDGB6CyJF1tkNcrUgAYXtZc-1PB53t-EgK4p0Cs2w8RDjKG",c="chmln",i=d.createElement("script");if(w[c]||(w[c]={}),!w[c].root){w[c].accountToken=t,w[c].location=w.location.href.toString(),w[c].now=new Date,w[c].fastUrl='https://fast.chameleon.io/';var m="identify alias track clear set show on off custom help _data".split(" ");for(var s=0;s<m.length;s++){!function(){var t=w[c][m[s]+"_a"]=[];w[c][m[s]]=function(){t.push(arguments);};}();}i.src=w[c].fastUrl+"messo/"+t+"/messo.min.js",i.async=!0,d.head.appendChild(i);}}(document,window);

    /* trychameleon.com user identification and data */

    // IMPORTANT: Replace USER.ID_IN_DB, USER.EMAIL, USER.FULL_NAME below with your app's actual variable names.

    chmln.identify('690b80e5f433ea81b96c9bf6', {   // REQUIRED, the unique ID of each user in your database (e.g. 23443 or "690b80e5f433ea81b96c9bf6")
    })
});