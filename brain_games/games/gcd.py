from brain_games.brain_engine import game_engine
from random import randint


game_description = 'Find the greatest common divisor of given numbers.'

def get_gcd(a, b):
    first_num = a
    second_num = b

    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num

    return first_num + second_num


def game_mode():
    first_number = randint(1, 100)
    second_number = randint(1, 100)

    question = f'{first_number} {second_number}'
    correct_answer = get_gcd(first_number, second_number)

    return (question, str(correct_answer))


def run_game():
    game_engine(game_mode, game_description)
