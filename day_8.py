r""" Day 8

>>> sample_input = 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2'
>>> solve_1(sample_input)
13

>>> bigger_sample = 'R 5\nU 8\nL 8\nD 3\nR 17\nD 10\nL 25\nU 20'
>>> solve_2(bigger_sample)
36
"""

from dataclasses import dataclass


@dataclass
class Cordinate:
    x: int = 0
    y: int = 0

    def _tuple(self):
        return (self.x, self.y)


class Rope:
    def __init__(self, length=1):
        self.loc = Cordinate()
        if length > 0:
            self.tail = Rope(length - 1)
        else:
            self.tail = None

    def __repr__(self):
        r = f'({self.loc.x}, {self.loc.y})'
        if self.tail:
            r += f', {self.tail.__repr__()}'
        return r

    def get_tail(self, num):
        if num == 0:
            return self
        else:
            return self.tail.get_tail(num - 1)

    def move(self, direction):
        """
        >>> r = Rope()
        >>> r.move('R')
        (1, 0), (0, 0)
        >>> r.move('R')
        (2, 0), (1, 0)
        >>> r.move('L')
        (1, 0), (1, 0)
        >>> r.move('U')
        (1, 1), (1, 0)
        >>> r.move('D')
        (1, 0), (1, 0)
        >>> r.move('D')
        (1, -1), (1, 0)
        >>> r.move('D')
        (1, -2), (1, -1)
        >>> r.move('R')
        (2, -2), (1, -1)
        >>> r.move('R')
        (3, -2), (2, -2)
        """
        # update loc
        if direction == 'U':
            self.loc.y += 1
        elif direction == 'D':
            self.loc.y -= 1
        elif direction == 'L':
            self.loc.x -= 1
        elif direction == 'R':
            self.loc.x += 1
        
        self._update_tail()

        return self

    def _update_tail(self):
        if self.tail is None:
            return

        dist_x = self.loc.x - self.tail.loc.x
        dist_y = self.loc.y - self.tail.loc.y

        if abs(dist_x) > 1 or abs(dist_y) > 1:
            # not touching
            if dist_x != 0:
                self.tail.loc.x += 1 if dist_x > 0 else -1
            if dist_y != 0:
                self.tail.loc.y += 1 if dist_y > 0 else -1

        self.tail._update_tail()

        return self



def solve_1(_in):
    rope = Rope()
    tail_history = set()
    for line in _in.split('\n'):
        direction, quantity = line.split(' ')
        quantity = int(quantity)
        for _ in range(quantity):
            rope.move(direction)
            tail_history.add(rope.tail.loc._tuple())
    return len(tail_history)


def solve_2(_in):
    rope = Rope(9)
    tail_history = set()
    for line in _in.split('\n'):
        direction, quantity = line.split(' ')
        quantity = int(quantity)
        for _ in range(quantity):
            rope.move(direction)
            tail_history.add(rope.get_tail(9).loc._tuple())
    return len(tail_history)



if __name__ == "__main__":
    with open('input/8.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')
