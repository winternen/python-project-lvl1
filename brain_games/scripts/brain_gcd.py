#!/usr/bin/env python
from brain_games.brain_engine import game_engine
from brain_games.games import gcd


def main():
    game_engine(gcd)


if __name__ == '__main__':
    main()
