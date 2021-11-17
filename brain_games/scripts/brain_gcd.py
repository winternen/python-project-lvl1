#!/usr/bin/env python
from brain_games.brain_engine import run_game
from brain_games.games import gcd


def main():
    run_game(gcd)


if __name__ == '__main__':
    main()
