from random import randint
from random import choice


description = 'What is the result of the expression?'


def generate_operator():
    operators = ('+', '-', '*')
    return choice(operators)


def generate_game():
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    operator = generate_operator()

    expression_result = {
        '+': first_operand + second_operand,
        '-': first_operand - second_operand,
        '*': first_operand * second_operand
    }

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(expression_result[operator])

    return question, correct_answer
