from random import randint


description = 'What number is missing in the progression?'


def get_progression(begin, step, length):
    result = []
    number = begin

    while len(result) < length:
        result.append(number)
        number += step

    return result


def generate_game():
    first_number = randint(1, 100)
    step = randint(1, 100)
    length = randint(5, 10)

    progression = get_progression(first_number, step, length)
    hidden_char = '..'
    hidden_pos = randint(0, len(progression) - 1)

    correct_answer = str(progression[hidden_pos])
    progression[hidden_pos] = hidden_char
    question = ' + '.join(map(str, progression))

    return question, correct_answer
