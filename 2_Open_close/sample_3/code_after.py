def print_quiz(questions):
    for q in questions:
        print(q.description)
        q.print_question_choices()
        print('')


class BooleanQuestion:
    def __init__(self, description):
        self.description = description

    def print_question_choices(self):
        print('1. True')
        print('2. False')


class MultipleChoiceQuestion:
    def __init__(self, description, options):
        self.description = description
        self.options = options

    def print_question_choices(self):
        for i, item in enumerate(self.options):
            print(f'{i + 1}. {item}')


class TextQuestion:
    def __init__(self, description):
        self.description = description

    def print_question_choices(self):
        print('Answer: __________________')


class RangeQuestion:
    def __init__(self, description):
        self.description = description

    def print_question_choices(self):
        print('Minimum: __________________')
        print('Maximum: __________________')


if __name__ == '__main__':
    questions = [
        BooleanQuestion('This video is useful.'),
        MultipleChoiceQuestion('What is your favorite language?', ['CSS', 'HTML', 'JS', 'Python']),
        TextQuestion('Describe your favorite JS feature.'),
        RangeQuestion('What is the speed limit in your city?'),  # new type of question to support
    ]
    print_quiz(questions)
