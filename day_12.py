r""" Day 12 - Breadth-first search

>>> _in = 'Sabqponm\nabcryxxl\naccszExk\nacctuvwj\nabdefghi'
>>> solve_1(_in)
31
>>> solve_2(_in)
29
"""

from collections import defaultdict
from dataclasses import dataclass
from typing import List


DIRECTIONS = [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]


@dataclass
class Point:
    height: str
    x: int
    y: int
    visited: bool


class HeightMap:
    points: List[List[Point]] = []
    start: Point = None
    end: Point = None

    def __init__(self, _in: str, end_height='z'):
        for x, row in enumerate(_in.split('\n')):
            point_row = []
            for y, height in enumerate(row):
                point = Point(height, x, y, False)
                if height == 'S':
                    point.height = 'a'
                    self.start = point
                elif height == 'E':
                    point.height = end_height
                    self.end = point
                point_row.append(point)
            self.points.append(point_row)
    
    def __repr__(self) -> str:
        out = []
        for row in self.points:
            out.append(''.join([p.height for p in row]))
        return '\n'.join(out)


def run_bfs(height_map: HeightMap, part_2_reset=False):
    initial_index = 0
    # TDOD!! BUG!! There's some kinda off-by-one error? sample input needs queue step to start at 1; real input needs queue step to start at 0
    queue = [(height_map.start, initial_index)]  # Point, steps
    while queue:
        loc, step = queue.pop(0)
        if loc == height_map.end:
            return loc, step
        for x, y in DIRECTIONS:
            try:
                next = height_map.points[loc.x + x][loc.y + y]
                if not next.visited:
                    distance = ord(next.height) - ord(loc.height)
                    if distance <= 1:
                        if part_2_reset and next.height == 'a':
                            queue.insert(0, (next, initial_index))
                        else:
                            queue.append((next, step + 1))
                        next.visited = True
            except IndexError:
                pass  # out of bounds; no need to check



def solve_1(_in: str):
    height_map = HeightMap(_in)
    _, distance = run_bfs(height_map, False)
    return distance
    

def solve_2(_in: str):
    height_map = HeightMap(_in)
    _, distance = run_bfs(height_map, True)
    return distance


if __name__ == "__main__":
    with open('input/12.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')