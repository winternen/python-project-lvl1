from random import randint


description = 'Answer "yes" if given number is prime. Otherwise answer "no".'


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
    question = randint(1, 1000)
    correct_answer = 'yes' if is_prime(question) else 'no'

    return question, correct_answer
