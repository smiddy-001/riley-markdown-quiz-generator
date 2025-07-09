"""
Quiz generator class that handles the conversion of markdown files to HTML quizzes.
"""

import os
from pathlib import Path
from typing import List, Optional

import markdown
from jinja2 import Environment, FileSystemLoader, select_autoescape

from .config import Config
from .template_manager import TemplateManager


class QuizGenerator:
    """Main quiz generator class."""

    def __init__(self, config: Config):
        """Initialize the quiz generator with configuration."""
        self.config = config
        self.template_manager = TemplateManager(config)
        config.ensure_directories()

    def process_all_files(self) -> List[str]:
        """Process all markdown files in the lookup folder."""
        processed_files = []
        lookup_path = Path(self.config.lookup_folder)

        if not lookup_path.exists():
            raise FileNotFoundError(f"Lookup folder '{self.config.lookup_folder}' does not exist")

        # Find all markdown files
        markdown_files = list(lookup_path.glob("**/*.md"))

        if not markdown_files:
            return processed_files

        for md_file in markdown_files:
            try:
                self._process_single_file(md_file)
                processed_files.append(md_file.name)
                print(f"Converting to Markdown ({md_file.name}) ...")
            except Exception as e:
                print(f"Error processing {md_file.name}: {e}")
                continue

        return processed_files

    def _process_single_file(self, md_file: Path) -> None:
        """Process a single markdown file."""
        # Read markdown content
        with open(md_file, 'r', encoding='utf-8') as f:
            markdown_content = f.read()

        # Convert markdown to HTML
        html_content = self._markdown_to_html(markdown_content)

        # Render final HTML
        final_html = self.template_manager.render_quiz(
            content=html_content,
            wrapper_render=self.config.wrapper_render
        )

        # Write output file
        output_file = self._get_output_filename(md_file)
        output_path = Path(self.config.output_folder) / output_file

        # Ensure output directory exists
        output_path.parent.mkdir(parents=True, exist_ok=True)

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(final_html)

    def _markdown_to_html(self, markdown_content: str) -> str:
        """Convert markdown content to HTML using extensions."""
        return markdown.markdown(
            markdown_content,
            extensions=self.config.markdown_extensions,
            output_format="html5"
        )

    def _get_output_filename(self, md_file: Path) -> str:
        """Get the output HTML filename from the markdown filename."""
        return md_file.with_suffix('.html').name

    def process_single_quiz(self, markdown_content: str, output_filename: str) -> str:
        """Process a single quiz from markdown content."""
        html_content = self._markdown_to_html(markdown_content)
        final_html = self.template_manager.render_quiz(
            content=html_content,
            wrapper_render=self.config.wrapper_render
        )

        # Write to output file if filename provided
        if output_filename:
            output_path = Path(self.config.output_folder) / output_filename
            output_path.parent.mkdir(parents=True, exist_ok=True)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(final_html)

        return final_html