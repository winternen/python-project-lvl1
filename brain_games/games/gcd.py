from random import randint


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
START_RANGE = 1
MAX_RANGE = 100


def get_gcd(a, b):
    first_num = a
    second_num = b

    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num %= second_num
        else:
            second_num %= first_num

    return first_num + second_num


def generate_game():
    first_number = randint(START_RANGE, MAX_RANGE)
    second_number = randint(START_RANGE, MAX_RANGE)

    question = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))

    return question, correct_answer
