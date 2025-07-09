"""
Quiz Generator Package
A modular, OOP-compliant Python system for generating HTML quizzes from markdown files.
"""

from .config import Config
from .quiz_generator import QuizGenerator
from .template_manager import TemplateManager
from .html_elements import *

__version__ = "1.0.0"
__author__ = "Riley Smith"

__all__ = [
    'Config',
    'QuizGenerator',
    'TemplateManager',
    'HTMLElement',
    'Button',
    'Input',
    'Label',
    'ListItem',
    'UnorderedList',
    'Div'
]