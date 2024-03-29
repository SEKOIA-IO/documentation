import re
import string

import mkdocs

TEMPLATE = string.Template(
    """
<style>
    .md-typeset h1,
    .md-content__button,
    .md-footer {
        display: none;
    }
    .md-main__inner {
        max-width: 100%;
        margin: 0;
    }

    .api-content {
        height: calc(100vh - 5.6rem) !important;
        overflow: auto;
    }
    .menu-content {
        height: calc(100vh - 5.6rem) !important;
    }

    redoc {
        display: block;
        isolation: isolate;
    }

</style>
<div>
    <div class="self-contained-css" id="redoc-container">

    </div>
</div>
<script src="https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js"> </script>

<script>
Redoc.init('$path', {
    hideLoading: true,
    theme: {
        rightPanel: {
            backgroundColor: "#992a85"
        }
    }
    }, document.getElementById('redoc-container'))


document.getElementsByTagName('article')[0].classList.add('api')
document.getElementsByTagName('article')[0].classList.remove('md-typeset')
document.querySelector('.api h1').remove()
</script>

"""
)

TOKEN = re.compile(r"!!redoc(?: (?P<path>https?://[^\s]+))?!!")


class RedocPlugin(mkdocs.plugins.BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        match = TOKEN.search(markdown)

        if match is None:
            return markdown

        path = match.group("path")

        pre_token = markdown[: match.start()]

        post_token = markdown[match.end() :]

        markdown = pre_token + TEMPLATE.substitute(path=path) + post_token

        return self.on_page_markdown(markdown, page, config, files)
