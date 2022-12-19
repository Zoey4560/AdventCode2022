r""" Day 8

>>> sample_input = 'R 4\nU 4\nL 3\nD 1\nR 4\nD 1\nL 5\nR 2'
>>> solve_1(sample_input)
13

"""

from dataclasses import dataclass


@dataclass
class Cordinate:
    x: int = 0
    y: int = 0

    def _tuple(self):
        return (self.x, self.y)


class Rope:
    def __init__(self):
        self.head = Cordinate()
        self.tail = Cordinate()

    def __repr__(self):
        return f'({self.head.x}, {self.head.y}), ({self.tail.x}, {self.tail.y})'

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
        # update head
        if direction == 'U':
            self.head.y += 1
        elif direction == 'D':
            self.head.y -= 1
        elif direction == 'L':
            self.head.x -= 1
        elif direction == 'R':
            self.head.x += 1
        
        # update tail
        dist_x = self.head.x - self.tail.x
        dist_y = self.head.y - self.tail.y

        if abs(dist_x) > 1 or abs(dist_y) > 1:
            # not touching
            if dist_x != 0:
                self.tail.x += 1 if dist_x > 0 else -1
            if dist_y != 0:
                self.tail.y += 1 if dist_y > 0 else -1
        return self



def solve_1(_in):
    rope = Rope()
    tail_history = set()
    for line in _in.split('\n'):
        direction, quantity = line.split(' ')
        quantity = int(quantity)
        for _ in range(quantity):
            rope.move(direction)
            tail_history.add(rope.tail._tuple())
    return len(tail_history)


def solve_2(_in):
    pass



if __name__ == "__main__":
    with open('input/8.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')
