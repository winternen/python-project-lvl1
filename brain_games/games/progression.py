from brain_games.brain_engine import game_engine
from random import randint


game_description = 'What number is missing in the progression?'


def get_progression(begin, step, length):
    result = []
    number = begin

    while len(result) < length:
        result.append(number)
        number += step

    return result


def game_mode():
    first_number = randint(1, 100)
    step = randint(1, 100)
    length = randint(5, 10)

    progression = get_progression(first_number, step, length)
    hidden_pos = randint(0, len(progression) - 1)
    hidden_char = '..'

    correct_answer = str(progression[hidden_pos])
    progression[hidden_pos] = hidden_char
    question = ' + '.join(map(str, progression))

    return (question, correct_answer)


def run_game():
    game_engine(game_mode, game_description)
