window.addEventListener("DOMContentLoaded", (event) => {
  // prettier-ignore
  !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
  posthog.init("phc_adBekSlnN2US9CpINrlyXZ651aXRMdReihHA5pi2Jdt", {
    api_host: "https://flags.sekoia.io",
    opt_in_site_apps: true,
  });

  // posthog surveys IDs
  const SURVEY_ID_UP = "019baa85-6cd8-0000-0919-c62dbbfa7e8f";
  const SURVEY_ID_DOWN = "019baa83-c271-0000-4550-e787f0a88e4e";

  // PostHog feedback survey
  document.addEventListener(
    "click",
    (e) => {
      const el = e.target.closest(".docs-feedback");
      if (!el) return;

      e.preventDefault();

      const vote = el.dataset.vote; // "up" | "down"

      // 3) Show instantly (no waiting for event-based condition evaluation)
      const surveyId = vote === "up" ? SURVEY_ID_UP : SURVEY_ID_DOWN;

      if (typeof posthog.displaySurvey === "function") {
        posthog.displaySurvey(surveyId);
      }
    },
    true
  );

  // PostHog search tracking
  const search = document.querySelector(".md-search");
  let debounceTimeout = null;
  new MutationObserver(() => {
    if (debounceTimeout) clearTimeout(debounceTimeout);
    debounceTimeout = setTimeout(() => {
      const results =
        parseInt(
          search
            .querySelector(".md-search-result__meta")
            ?.innerText?.trim()
            ?.replaceAll(/\D/g, "")
        ) || 0;
      const query = search.querySelector("input.md-search__input").value.trim();

      posthog.capture("search", {
        search_query: query,
        result_count: results,
      });
      debounceTimeout = null;
    }, 1000);
  }).observe(search, { childList: true, subtree: true });
});
