from brain_games.brain_engine import game_engine
from random import randint


game_description = 'What is the result of the expression?'


def random_operator():
    operators = ('+', '-', '*')
    coll_size = len(operators) - 1
    return operators[randint(0, coll_size)]


def game_mode():
    first_operand = randint(1, 100)
    second_operand = randint(1, 100)
    operator = random_operator()

    expression_result = {
        '+': first_operand + second_operand,
        '-': first_operand - second_operand,
        '*': first_operand * second_operand
    }

    question = f'{first_operand} {operator} {second_operand}'
    correct_answer = str(expression_result[operator])

    return (question, correct_answer)


def run_game():
    game_engine(game_mode, game_description)
