from random import randint


DESCRIPTION = 'What number is missing in the progression?'
START_RANGE = 1
MAX_RANGE = 100


def get_progression(begin, step, length):
    result = []
    number = begin

    while len(result) < length:
        result.append(number)
        number += step

    return result


def hide_progression_number(list):
    progression = list
    progression_len = len(progression) - 1

    hidden_pos = randint(0, progression_len)
    hidden_char = '..'
    hidden_number = str(progression[hidden_pos])

    progression[hidden_pos] = hidden_char
    hidden_progression = ' '.join(map(str, progression))

    return hidden_number, hidden_progression


def generate_game():
    first_number = randint(START_RANGE, MAX_RANGE)
    step = randint(START_RANGE, MAX_RANGE)
    progression_length = randint(5, 10)
    progression = get_progression(first_number, step, progression_length)

    correct_answer, question = hide_progression_number(progression)

    return question, correct_answer
