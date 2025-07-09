"""
Quiz Generator - Main Entry Point
Developed by Osanda Deshan
Enhanced with OOP design
"""

import sys
import os
from pathlib import Path

from src.quiz_generator import QuizGenerator
from src.config import Config


def main():
    """Main entry point for the quiz generator."""
    print("-" * 50)
    print("Markdown Quiz Generator v1.0 (OOP Edition)")
    print("-" * 50)

    # Check for embed mode
    embed_mode = 'embed' in sys.argv

    # Initialize configuration
    config = Config(
        lookup_folder='./markdown-quiz-files',
        output_folder='./docs',
        wrapper_render=not embed_mode
    )

    # Create quiz generator
    generator = QuizGenerator(config)

    # Process all markdown files
    try:
        processed_files = generator.process_all_files()

        if processed_files:
            print(f"\nSuccessfully processed {len(processed_files)} files:")
            for file_name in processed_files:
                print(f"  - {file_name}")
        else:
            print("No markdown files found to process.")

    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

    print("\nQuiz generation completed successfully!")
    sys.exit(0)


if __name__ == "__main__":
    main()