"""
Checkbox extension for markdown processing.
Converts markdown checkbox syntax to HTML checkbox inputs.
"""

import re
from markdown.extensions import Extension
from markdown.postprocessors import Postprocessor

from ..html_elements import Input, Label, ListItem


def makeExtension(configs=None):
    """Create the checkbox extension."""
    if configs is None:
        return CheckboxExtension()
    else:
        return CheckboxExtension(configs=configs)


class CheckboxExtension(Extension):
    """Extension for processing checkbox questions in markdown."""

    def __init__(self, **kwargs):
        """Initialize the extension with configuration."""
        self.config = {
            "list_class": ["checklist", "class name to add to the list element"],
            "render_item": [render_item, "custom function to render items"]
        }
        super().__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        """Add the checkbox postprocessor to markdown."""
        list_class = self.getConfig("list_class")
        renderer = self.getConfig("render_item")
        postprocessor = CheckboxPostprocessor(list_class, renderer, md)
        md.postprocessors.register(postprocessor, "checklist", 175)


class CheckboxPostprocessor(Postprocessor):
    """Postprocessor that converts checkbox markdown to HTML."""

    def __init__(self, list_class, render_item, *args, **kwargs):
        """Initialize the postprocessor."""
        self.list_class = list_class
        self.render_item = render_item
        super().__init__(*args, **kwargs)

        # Regex patterns for matching checkbox lists and items
        self.list_pattern = re.compile(r"(<ul>\n<li>\[[ Xx]\])")
        self.item_pattern = re.compile(r"^<li>\[([ Xx])\](.*)</li>$", re.MULTILINE)

    def run(self, html):
        """Process the HTML and convert checkbox patterns."""
        html = re.sub(self.list_pattern, self._convert_list, html)
        return re.sub(self.item_pattern, self._convert_item, html)

    def _convert_list(self, match):
        """Convert list opening tag to include checkbox class."""
        return match.group(1).replace("<ul>", f"<ul class=\"{self.list_class}\">")

    def _convert_item(self, match):
        """Convert list item to checkbox input."""
        state, caption = match.groups()
        return self.render_item(caption, state != " ")


def render_item(caption, checked):
    """Render a checkbox item using HTML element classes."""
    correct = "1" if checked else "0"
    fake = "0" if checked else "1"

    # Create checkbox input using HTML element class
    checkbox = Input(
        input_type="checkbox",
        data_attributes={
            "question": fake,
            "content": correct
        }
    ).add_class("checkbox")

    # Create label with checkbox and caption
    label = Label(content=checkbox.render() + caption)

    # Create list item
    list_item = ListItem(content=label.render())

    return list_item.render()