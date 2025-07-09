"""
Configuration management for the quiz generator.
"""

from dataclasses import dataclass
from pathlib import Path
from typing import List


@dataclass
class Config:
    """Configuration settings for the quiz generator."""

    lookup_folder: str = './markdown-quiz-files'
    output_folder: str = './docs'
    wrapper_render: bool = True
    template_folder: str = 'templates'
    static_folder: str = 'static'

    # Markdown extensions to use
    markdown_extensions: List[str] = None

    def __post_init__(self):
        """Initialize default markdown extensions if not provided."""
        if self.markdown_extensions is None:
            self.markdown_extensions = [
                "tables",
                "src.extensions.checkbox",
                "src.extensions.radio",
                "src.extensions.textbox"
            ]

    def ensure_directories(self):
        """Create necessary directories if they don't exist."""
        Path(self.lookup_folder).mkdir(parents=True, exist_ok=True)
        Path(self.output_folder).mkdir(parents=True, exist_ok=True)
        Path(self.template_folder).mkdir(parents=True, exist_ok=True)
        Path(self.static_folder).mkdir(parents=True, exist_ok=True)