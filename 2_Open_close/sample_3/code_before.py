"""
We need to modify print_quiz() function any time
new type of question need to be supported.
"""


def print_quiz(questions):
    for q in questions:
        print(q['description'])
        if q['type'] == 'boolean':
            print('1. True')
            print('2. False')
        elif q['type'] == 'multiple_choice':
            for i, item in enumerate(q['options']):
                print(f'{i + 1}. {item}')
        elif q['type'] == 'text':
            print('Answer: __________________')
        # new code to support new question type
        elif q['type'] == 'range':
            print('Minimum: __________________')
            print('Maximum: __________________')
        print('')


if __name__ == '__main__':
    questions = [
        {
            'type': 'boolean',
            'description': 'This video is useful.'
        },
        {
            'type': 'multiple_choice',
            'description': 'What is your favorite language?',
            'options': ['CSS', 'HTML', 'JS', 'Python']
        },
        {
            'type': 'text',
            'description': 'Describe your favorite JS feature.'
        },
        # new type of question to support
        {
            'type': 'range',
            'description': 'What is the speed limit in your city?'
        }
    ]
    print_quiz(questions)
