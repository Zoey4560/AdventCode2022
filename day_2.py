r"""Going object oriented-ish for this, if we're gonna be doing gameplay
 useful for ipython dev
> from importlib import reload

>>> play_tourney_v1('A Y\nB X\nC Z')
15
>>> play_tourney_v2('A Y\nB X\nC Z')
12
"""

from enum import auto, IntEnum

"""Enums acting both as enums and stores for point values for scoring `the shape you select` and `the outcome of the round`"""
class Shape(IntEnum):
    rock = 1
    paper = 2
    scisors = 3

    def beats(self):
        return {
            Shape.rock: Shape.scisors,
            Shape.scisors: Shape.paper,
            Shape.paper: Shape.rock
        }[self]
    
    def needs(self, desired_outcome):
        """poorly named method that tells what you need to play in response to Shape to cause the desired outcome"""
        if desired_outcome is Outcome.draw:
            return self
        if desired_outcome is Outcome.loss:
            return self.beats()
        return self.beats().beats()


class Outcome(IntEnum):
    win = 6
    draw = 3
    loss = 0

    @classmethod
    def of_round(cls, their_move, your_move):
        if your_move is their_move:
            return cls.draw
        elif your_move.beats() == their_move:
            return cls.win
        return cls.loss


"""v1 and v2 for part 1 and 2 of the problem"""

def _decode_v1(code):
    return {
        'A': Shape.rock,
        'X': Shape.rock,
        'B': Shape.paper,
        'Y': Shape.paper,
        'C': Shape.scisors,
        'Z': Shape.scisors,
    }[code]

def _decode_v2(code):
    return {
        'A': Shape.rock,
        'X': Outcome.loss,
        'B': Shape.paper,
        'Y': Outcome.draw,
        'C': Shape.scisors,
        'Z': Outcome.win,
    }[code]

def decode_input(_in, decoder):
    coded_moveset = [x.split(' ') for x in _in.split('\n')]
    moveset = [ (decoder(x), decoder(y)) for (x, y) in coded_moveset]
    return moveset

def score(moveset):
    return sum([ you + Outcome.of_round(them, you) for them, you in moveset ])

def play_tourney_v1(_in):
    moveset = decode_input(_in, _decode_v1)
    return score(moveset)

def play_tourney_v2(_in):
    strategy_guide = decode_input(_in, _decode_v2)
    moveset = [ (them, them.needs(outcome)) for (them, outcome) in strategy_guide]
    return score(moveset)


if __name__ == "__main__":
    with open('input/2.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {play_tourney_v1(_in)}')
        print(f'Part 2: {play_tourney_v2(_in)}')