$(function(){
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
});