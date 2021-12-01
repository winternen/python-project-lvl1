from random import randint


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
START_RANGE = 1
MAX_RANGE = 100


def is_even(number):
    return number % 2 == 0


def generate_game():
    random_number = randint(START_RANGE, MAX_RANGE)

    question = random_number
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer
