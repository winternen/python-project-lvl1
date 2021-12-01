from random import randint
from random import choice


DESCRIPTION = 'What is the result of the expression?'
START_RANGE = 1
MAX_RANGE = 100


def generate_operator():
    operators = ('+', '-', '*')
    return choice(operators)


def generate_game():
    first_operand = randint(START_RANGE, MAX_RANGE)
    second_operand = randint(START_RANGE, MAX_RANGE)
    operator = generate_operator()

    expression_result = {
        '+': first_operand + second_operand,
        '-': first_operand - second_operand,
        '*': first_operand * second_operand
    }

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(expression_result[operator])

    return question, correct_answer
