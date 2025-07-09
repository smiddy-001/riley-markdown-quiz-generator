"""
Template management for rendering HTML templates.
"""

from pathlib import Path
from jinja2 import Environment, FileSystemLoader, select_autoescape, Template

from .config import Config
from .html_elements import Button, Div


class TemplateManager:
    """Manages HTML templates and rendering."""

    def __init__(self, config: Config):
        """Initialize template manager with configuration."""
        self.config = config
        self._ensure_templates_exist()

        # Initialize Jinja2 environment
        self.env = Environment(
            loader=FileSystemLoader(config.template_folder),
            autoescape=select_autoescape(['html', 'xml'])
        )

    def _ensure_templates_exist(self):
        """Create default templates if they don't exist."""
        template_path = Path(self.config.template_folder)
        template_path.mkdir(parents=True, exist_ok=True)

        # Create base template
        base_template_path = template_path / 'base.html'
        if not base_template_path.exists():
            with open(base_template_path, 'w', encoding='utf-8') as f:
                f.write(self._get_base_template())

        # Create wrapper template
        wrapper_template_path = template_path / 'wrapper.html'
        if not wrapper_template_path.exists():
            with open(wrapper_template_path, 'w', encoding='utf-8') as f:
                f.write(self._get_wrapper_template())

        # Create JavaScript file
        static_path = Path(self.config.static_folder)
        static_path.mkdir(parents=True, exist_ok=True)

        js_file_path = static_path / 'app.js'
        if not js_file_path.exists():
            with open(js_file_path, 'w', encoding='utf-8') as f:
                f.write(self._get_javascript_content())

    def render_quiz(self, content: str, wrapper_render: bool = True) -> str:
        """Render a complete quiz HTML page."""
        # Get JavaScript content
        javascript = self._get_javascript_content()

        # Render base template
        base_template = self.env.get_template('base.html')
        quiz_html = base_template.render(content=content, javascript=javascript)

        # Wrap in wrapper template if needed
        if wrapper_render:
            wrapper_template = self.env.get_template('wrapper.html')
            quiz_html = wrapper_template.render(content=quiz_html)

        return quiz_html

    def _get_base_template(self) -> str:
        return '''<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Quiz</title>
        <link href="https://cdn.jsdelivr.net/npm/daisyui@5" rel="stylesheet" type="text/css" />
        <script src="https://cdn.tailwindcss.com"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.2.1/flowbite.min.js"></script>
        <link rel="stylesheet" href="https://latex.vercel.app/style.css">
        <script src="https://code.jquery.com/jquery-3.6.0.min.js"
                integrity="sha256-/xUj+3OJU5yExlq6GSYGSHk7tPXikynS7ogEvDej/m4="
                crossorigin="anonymous"></script>
    </head>
    <body class="flex min-h-screen bg-white text-base-content">

        <!-- Sidebar -->
        <div class="w-64 p-4">
            <h2 class="text-xl font-bold mb-4">Navigation</h2>

            <!-- Dropdown for each course -->
            {% for course in ['COSC261', 'SENG201', 'SENG365', 'MATH220'] %}
            <div class="!visible collapse collapse-arrow mb-2">
                <input type="checkbox" class="peer" id="collapse-{{ course|lower }}" />
                <div class="collapse-title font-medium peer-checked:bg-base-200">
                    {{ course }}
                </div>
                <div class="collapse-content hidden peer-checked:block">
                    <ul class="menu">
                        {% for i in range(1, 12) %}
                        <li><a href="./{{ course|lower }}_w{{ i }}.html">{{ course }} Week {{ i }}</a></li>
                        {% endfor %}
                    </ul>
                </div>
            </div>
            {% endfor %}
        </div>

        <!-- Main content -->
        <div class="flex-1 p-6">
            {{ content | safe }}
            <script type="text/javascript">{{ javascript | safe }}</script>
        </div>
    </body>
    </html>'''

    def _get_wrapper_template(self) -> str:
        """Get the wrapper template content with Tailwind styling."""
        return '''<div class="container mx-auto max-w-4xl p-6">
    <div class="rounded-lg shadow-sm p-8">
        {{ content | safe }}
    </div>

    <!-- Score display -->
    <div id="tg-msg" class="alert mt-6 hidden" role="alert">
        <div class="flex items-center">
            <svg class="w-6 h-6 mr-2" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z" clip-rule="evenodd"></path>
            </svg>
            <div>
                <span id="tg-correct-questions"></span> Correct!
                <br><strong>Rating: <span id="tg-score"></span>%</strong>
            </div>
        </div>
    </div>

    <!-- Action buttons -->
    <div class="flex gap-4 mt-6">
        <button id="check-questions" class="btn" style="background: black; color: white">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
            </svg>
            Check Answers
        </button>
        <button id="reset-questions" class="btn btn-outline">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path>
            </svg>
            Reset All
        </button>
    </div>
</div>'''

    def _get_javascript_content(self) -> str:
        """Get the JavaScript content for quiz functionality."""
        return '''$(function(){
    // Initialize questions
    $('ul.radio-list, ul.checklist, ul.textbox').each(function(i, el){
        var questionClass = $(this).attr('class');
        $(this).parent().addClass('question-row').addClass(questionClass);

        if (questionClass === 'radio-list') {
            $(this).find('input[type="radio"]').attr('name', 'radio-question-' + i);
        }
    });

    function checkQuestion() {
        resetQuestions(true);
        var questions = $('li.question-row');
        var total_questions = questions.length;
        var correct = 0;

        questions.each(function(i, el) {
            var self = $(this);

            // Single choice questions (radio buttons)
            if (self.hasClass('radio-list')) {
                if (self.find('input[type="radio"][data-content="1"]:checked').length === 1) {
                    correct += 1;
                    self.addClass('border-l-4 border-success bg-success/10');
                } else {
                    self.addClass('border-l-4 border-error bg-error/10');
                }
            }

            // Text input questions
            if (self.hasClass('textbox')) {
                var textbox = self.find('input[type="text"]');
                var correct_text = String(textbox.data("content")).trim().split("").reverse().join("");

                if (String(textbox.val()).trim().toLowerCase() === correct_text.toLowerCase()) {
                    correct += 1;
                    self.addClass('border-l-4 border-success bg-success/10');
                } else {
                    self.addClass('border-l-4 border-error bg-error/10');
                    var correctSpan = textbox.parent().find("i.text-correct");
                    if (correctSpan.length === 0) {
                        textbox.after('<i class="text-correct ml-2 text-sm text-success">Correct: ' + correct_text + '</i>');
                    } else {
                        correctSpan.html('Correct: ' + correct_text);
                    }
                }
            }

            // Multiple choice questions (checkboxes)
            if (self.hasClass('checklist')) {
                var total_corrects = self.find('input[type="checkbox"][data-content="1"]').length;
                var total_incorrects = self.find('input[type="checkbox"][data-content="0"]').length;
                var correct_selected = self.find('input[type="checkbox"][data-content="1"]:checked').length;
                var incorrect_selected = self.find('input[type="checkbox"][data-content="0"]:checked').length;

                var qc = +((correct_selected / total_corrects) - (incorrect_selected / total_incorrects)).toFixed(2);
                if (qc < 0) qc = 0;

                correct += qc;

                if (qc === 0) {
                    self.addClass('border-l-4 border-error bg-error/10');
                } else if (qc > 0 && qc < 1) {
                    self.addClass('border-l-4 border-warning bg-warning/10');
                } else {
                    self.addClass('border-l-4 border-success bg-success/10');
                }
            }
        });

        showScore(correct, total_questions);
    }

    function showScore(correct, total) {
        var score = Math.round((correct / total) * 100);
        var msgClasses = 'alert-error';

        if (score >= 70) {
            msgClasses = 'alert-success';
        } else if (score >= 50) {
            msgClasses = 'alert-warning';
        }

        $('#tg-correct-questions').text(correct.toFixed(1) + ' out of ' + total);
        $('#tg-score').text(score);
        $('#tg-msg').removeClass('alert-error alert-success alert-warning')
                   .addClass(msgClasses)
                   .removeClass('hidden');
    }

    function resetQuestions(keep) {
        $('li.question-row').removeClass('border-l-4 border-success bg-success/10 border-error bg-error/10 border-warning bg-warning/10');
        $('i.text-correct').remove();
        $('#tg-msg').removeClass('alert-error alert-success alert-warning').addClass('hidden');

        if (keep === true) {
            return;
        }

        $('li.question-row').find('input[type="text"]').val('');
        $('li.question-row').find('input[type="radio"], input[type="checkbox"]').prop('checked', false);
    }

    // Event handlers
    $('#check-questions').on('click', checkQuestion);
    $('#reset-questions').on('click', resetQuestions);
});'''

    def create_quiz_buttons(self) -> str:
        """Create quiz control buttons using HTML element classes."""
        check_button = Button(
            content="Check Answers",
            button_type="button"
        ).add_class("btn").add_class("btn-primary").add_class("bg-black").set_attribute("id", "check-questions")

        reset_button = Button(
            content="Reset All",
            button_type="button"
        ).add_class("btn").add_class("btn-outline").set_attribute("id", "reset-questions")

        button_container = Div().add_class("flex").add_class("gap-4").add_class("mt-6")
        button_container.add_child(check_button)
        button_container.add_child(reset_button)

        return button_container.render()