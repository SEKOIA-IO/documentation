from markdown import Extension
from markdown.treeprocessors import Treeprocessor
from xml.etree.ElementTree import Element
import re


class ImagesTreeprocessor(Treeprocessor):
    """
    Rewritten from https://github.com/g-provost/lightgallery-markdown
    to be compatible with python-markdown >= 3.3.7

    Enables lightgallery.js on image tags of the form ![!blah](img.png)
    """

    def __init__(self, md, config):
        super().__init__(md)
        self.re = re.compile(r"^!.*")
        self.config = config

    def run(self, root):
        parent_map = {c: p for p in root.iter() for c in p}
        images = root.iter("img")
        for image in images:
            desc = image.attrib.get("alt", "")
            if self.re.match(desc):
                desc = desc.lstrip("!")
                image.set("alt", desc)
                parent = parent_map[image]
                ix = list(parent).index(image)

                div_node = Element("div")
                div_node.set("class", "lightgallery")
                new_node = Element("a")
                new_node.set("href", image.attrib["src"])

                if self.config["show_description_in_lightgallery"]:
                    new_node.set("data-sub-html", desc)

                new_node.append(image)
                div_node.append(new_node)
                parent.insert(ix, div_node)
                parent.remove(image)

                if self.config["show_description_as_inline_caption"]:
                    inline_caption_node = Element("p")
                    inline_caption_node.set(
                        "class", self.config["custom_inline_caption_css_class"]
                    )
                    inline_caption_node.text = desc
                    parent.insert(ix + 1, inline_caption_node)


class LightGalleryExtension(Extension):
    def __init__(self, **kwargs):
        self.config = {
            "show_description_in_lightgallery": [
                True,
                "Adds the description as caption in lightgallery dialog. Default: True",
            ],
            "show_description_as_inline_caption": [
                False,
                "Adds the description as inline caption below the image. Default: False",
            ],
            "custom_inline_caption_css_class": [
                "",
                "Custom CSS classes which are applied to the inline caption paragraph. Multiple classes are separated via space. Default: empty",
            ],
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md):
        config = self.getConfigs()
        md.treeprocessors.register(ImagesTreeprocessor(md, config), "lightbox", 15)


def makeExtension(*_, **kwargs):
    return LightGalleryExtension(**kwargs)
