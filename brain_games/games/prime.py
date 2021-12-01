from random import randint


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
START_RANGE = 1
MAX_RANGE = 100


def is_prime(num):
    if num < 2:
        return False

    divisor = 2

    while divisor < num:
        if num % divisor == 0:
            return False
        else:
            divisor += 1

    return True


def generate_game():
    random_number = randint(START_RANGE, MAX_RANGE)

    question = random_number
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
