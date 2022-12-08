"""
v0: Going object oriented for this, if we're gonna be doing gameplay
v0.1                    ^ish

# useful for ipython dev
# > from importlib import reload
"""
from enum import auto, IntEnum

"""Enums acting both as enums and stores for point values for scoring `the shape you select` and `the outcome of the round`"""
class Shape(IntEnum):
    rock = 1
    paper = 2
    scisors = 3

    def beats(self, their_move):
        return {
            Shape.rock: Shape.scisors,
            Shape.scisors: Shape.paper,
            Shape.paper: Shape.rock
        }[self] == their_move


class Outcome(IntEnum):
    win = 6
    draw = 3
    loss = 0

    @classmethod
    def of_round(cls, their_move, your_move):
        if your_move is their_move:
            return cls.draw
        elif your_move.beats(their_move):
            return cls.win
        return cls.loss


def _decode(code):
    return {
        'A': Shape.rock,
        'X': Shape.rock,
        'B': Shape.paper,
        'Y': Shape.paper,
        'C': Shape.scisors,
        'Z': Shape.scisors,
    }[code]


def play_tourney(_in):
    coded_moveset = [x.split(' ') for x in _in.split('\n')]
    moveset = [ (_decode(them), _decode(you)) for (them, you) in coded_moveset]
    # TODO
    return moveset