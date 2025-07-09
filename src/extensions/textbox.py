"""
Textbox extension for markdown processing.
Converts markdown textbox syntax to HTML text inputs.
"""

import re
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

from ..html_elements import Input, ListItem


def makeExtension(configs=None):
    """Create the textbox extension."""
    if configs is None:
        return TextboxExtension()
    else:
        return TextboxExtension(configs=configs)


class TextboxExtension(Extension):
    """Extension for processing text input questions in markdown."""

    def __init__(self, **kwargs):
        """Initialize the extension with configuration."""
        self.config = {
            "list_class": ["textbox", "class name to add to the list element"],
            "render_item": [render_item, "custom function to render items"]
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        """Add the textbox postprocessor to markdown."""
        list_class = self.getConfig("list_class")
        renderer = self.getConfig("render_item")
        postprocessor = TextboxPostprocessor(list_class, renderer, md)
        md.postprocessors.register(postprocessor, "textbox", 175)


class TextboxPostprocessor(Postprocessor):
    """Postprocessor that converts textbox markdown to HTML."""

    def __init__(self, list_class, render_item, *args, **kwargs):
        """Initialize the postprocessor."""
        self.list_class = list_class
        self.render_item = render_item
        super().__init__(*args, **kwargs)

        # Regex patterns for matching textbox lists and items
        self.list_pattern = re.compile(r"(<ul>\n<li>[Rr]:=)")
        self.item_pattern = re.compile(r"^<li>([Rr]:=)(.*)</li>$", re.MULTILINE)

    def run(self, html):
        """Process the HTML and convert textbox patterns."""
        html = re.sub(self.list_pattern, self._convert_list, html)
        return re.sub(self.item_pattern, self._convert_item, html)

    def _convert_list(self, match):
        """Convert list opening tag to include textbox class."""
        return match.group(1).replace("<ul>", f"<ul class=\"{self.list_class}\">")

    def _convert_item(self, match):
        """Convert list item to text input."""
        state, caption = match.groups()
        return self.render_item(caption, state != " ")


def render_item(caption: str, value):
    """Render a textbox item using HTML element classes."""
    # The correct answer is stored reversed as metadata
    correct = caption.strip()[::-1]
    fake = "".join([c + 's' for c in correct])

    # Create text input using HTML element class
    textbox = Input(
        input_type="text",
        placeholder="Enter the correct answer.",
        data_attributes={
            "content": correct,
            "question": fake
        }
    ).add_class("input").add_class("input-bordered").add_class("w-full")

    # Create list item
    list_item = ListItem(content=textbox.render())

    return list_item.render()