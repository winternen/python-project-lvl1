from brain_games.brain_engine import game_engine
from random import randint


game_description = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def game_mode():
    question = randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return (question, correct_answer)


def run_game():
    game_engine(game_mode, game_description)
