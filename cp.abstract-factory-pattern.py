#!/usr/bin/env python

"""
Creational Pattern --> Abstract Factory Pattern

Provide interface for creating objects without specifying their concrete classes.
"""

import abc

class Game(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def players_required(self):
        pass


class Cricket(Game):

    def players_required(self):
        return 11

    def __str__(self):
        return self.__class__.__name__


class Chess(Game):

    def players_required(self):
        return 2

    def __str__(self):
        return self.__class__.__name__

class CricketFactory:

    def get_game(self):
        return Cricket()


class ChessFactory:

    def get_game(self):
        return Chess()


class PlayGames:

    def __init__(self, game_factory=None):
        self.game_factory = game_factory

    def play_game(self):
        game = self.game_factory.get_game()
        print(f"{game.players_required()} players are required to play {game}.")


if __name__ == "__main__":
    for game in [ChessFactory(), CricketFactory()]:
        game = PlayGames(game)
        game.play_game()

