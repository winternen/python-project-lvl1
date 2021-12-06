from random import randint


DESCRIPTION = 'What number is missing in the progression?'
START_RANGE, MAX_RANGE = 1, 100
MIN_LENGTH, MAX_LENGTH = 5, 10


def get_progression(begin, step, length):
    result = []
    number = begin

    while len(result) < length:
        result.append(number)
        number += step

    return result


def get_question(progression, index):
    hidden_progression = progression

    hidden_char = '..'
    hidden_progression[index] = hidden_char
    question = ' '.join(map(str, hidden_progression))

    return question


def generate_game():
    first_number = randint(START_RANGE, MAX_RANGE)
    step = randint(START_RANGE, MAX_RANGE)
    progression_length = randint(MIN_LENGTH, MAX_LENGTH)

    progression = get_progression(first_number, step, progression_length)
    hidden_pos = randint(0, progression_length - 1)

    correct_answer = str(progression[hidden_pos])
    question = get_question(progression, hidden_pos)

    return question, correct_answer
