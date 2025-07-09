"""
HTML element classes that correspond to HTML counterparts.
Each class represents an HTML element with its expected properties.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field


@dataclass
class HTMLElement(ABC):
    """Base class for all HTML elements."""

    tag: str = ""
    attributes: Dict[str, str] = field(default_factory=dict)
    css_classes: List[str] = field(default_factory=list)
    content: str = ""

    def add_class(self, css_class: str) -> 'HTMLElement':
        """Add a CSS class to the element."""
        if css_class not in self.css_classes:
            self.css_classes.append(css_class)
        return self

    def set_attribute(self, name: str, value: str) -> 'HTMLElement':
        """Set an attribute on the element."""
        self.attributes[name] = value
        return self

    def get_class_string(self) -> str:
        """Get the class attribute string."""
        return " ".join(self.css_classes) if self.css_classes else ""

    @abstractmethod
    def render(self) -> str:
        """Render the element to HTML string."""
        pass


@dataclass
class Button(HTMLElement):
    """HTML button element."""

    button_type: str = "button"
    onclick: Optional[str] = None
    disabled: bool = False

    def __post_init__(self):
        self.tag = "button"
        if self.button_type:
            self.set_attribute("type", self.button_type)
        if self.onclick:
            self.set_attribute("onclick", self.onclick)
        if self.disabled:
            self.set_attribute("disabled", "disabled")

    def render(self) -> str:
        """Render button to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        return f'<{self.tag}{attr_string}>{self.content}</{self.tag}>'


@dataclass
class Input(HTMLElement):
    """HTML input element."""

    input_type: str = "text"
    name: Optional[str] = None
    value: Optional[str] = None
    placeholder: Optional[str] = None
    data_attributes: Dict[str, str] = field(default_factory=dict)

    def __post_init__(self):
        self.tag = "input"
        self.set_attribute("type", self.input_type)

        if self.name:
            self.set_attribute("name", self.name)
        if self.value:
            self.set_attribute("value", self.value)
        if self.placeholder:
            self.set_attribute("placeholder", self.placeholder)

        # Add data attributes
        for key, value in self.data_attributes.items():
            self.set_attribute(f"data-{key}", value)

    def render(self) -> str:
        """Render input to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        return f'<{self.tag}{attr_string} />'


@dataclass
class Label(HTMLElement):
    """HTML label element."""

    for_attribute: Optional[str] = None

    def __post_init__(self):
        self.tag = "label"
        if self.for_attribute:
            self.set_attribute("for", self.for_attribute)

    def render(self) -> str:
        """Render label to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        return f'<{self.tag}{attr_string}>{self.content}</{self.tag}>'


@dataclass
class ListItem(HTMLElement):
    """HTML list item element."""

    def __post_init__(self):
        self.tag = "li"

    def render(self) -> str:
        """Render list item to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        return f'<{self.tag}{attr_string}>{self.content}</{self.tag}>'


@dataclass
class UnorderedList(HTMLElement):
    """HTML unordered list element."""

    items: List[ListItem] = field(default_factory=list)

    def __post_init__(self):
        self.tag = "ul"

    def add_item(self, item: ListItem) -> 'UnorderedList':
        """Add a list item to the list."""
        self.items.append(item)
        return self

    def render(self) -> str:
        """Render unordered list to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        # Render items
        items_html = "".join([item.render() for item in self.items])

        return f'<{self.tag}{attr_string}>{items_html}</{self.tag}>'


@dataclass
class Div(HTMLElement):
    """HTML div element."""

    children: List[HTMLElement] = field(default_factory=list)

    def __post_init__(self):
        self.tag = "div"

    def add_child(self, child: HTMLElement) -> 'Div':
        """Add a child element to the div."""
        self.children.append(child)
        return self

    def render(self) -> str:
        """Render div to HTML."""
        attrs = []

        # Add all attributes
        for name, value in self.attributes.items():
            attrs.append(f'{name}="{value}"')

        # Add classes
        if self.css_classes:
            attrs.append(f'class="{self.get_class_string()}"')

        attr_string = " " + " ".join(attrs) if attrs else ""

        # Render children
        children_html = "".join([child.render() for child in self.children])
        content_html = self.content + children_html

        return f'<{self.tag}{attr_string}>{content_html}</{self.tag}>'