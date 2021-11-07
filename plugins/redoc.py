import mkdocs
import string
import re

TEMPLATE = string.Template("""
<style>
    .md-typeset h1,
    .md-content__button {
        display: none;
    }
    .md-main__inner {
        max-width: 100%;
        margin: 0;
    }

    redoc {
        display: block;
    }
</style>
<div>
<redoc spec-url='$path' nativeScrollbars></redoc>
</div>
<script src="https://cdn.jsdelivr.net/npm/redoc@latest/bundles/redoc.standalone.js" native-scrollbars disable-search> </script>
</script>
<script>
    document.getElementsByTagName('article')[0].classList.add('api')
</script>
""")

TOKEN = re.compile(r"!!redoc(?: (?P<path>https?://[^\s]+))?!!")


class RedocPlugin(mkdocs.plugins.BasePlugin):
    def on_page_markdown(self, markdown, page, config, files):
        match = TOKEN.search(markdown)

        if match is None:
            return markdown

        path = match.group("path")
        
        pre_token = markdown[:match.start()]

        post_token = markdown[match.end():]

        markdown = pre_token + TEMPLATE.substitute(path=path) + post_token

        return self.on_page_markdown(markdown, page, config, files)