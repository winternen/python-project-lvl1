import prompt


ROUNDS_COUNT = 3


def run_game(game):
    print('Welcome to the Brain Games!')
    player_name = prompt.string('May I have your name? ')
    print(f'Hello, {player_name}')
    print(game.DESCRIPTION)

    for _ in range(ROUNDS_COUNT):
        (question, correct_answer) = game.generate_game()

        print(f'Question: {question}')
        player_answer = prompt.string('Your answer: ')

        if player_answer != correct_answer:
            print(f'"{player_answer}" is wrong answer ;(. '
                  f'Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {player_name}!')
            return
        else:
            print('Correct!')
    print(f'Congratulations, {player_name}!')
