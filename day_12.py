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
    points: List[List[Point]]
    start: Point
    end: Point

    def __init__(self, _in: str, end_height='z'):
        self.points = []
        for x, row in enumerate(_in.split('\n')):
            point_row = []
            for y, height in enumerate(row):
                point = Point(height, x, y, False)
                if height == 'S':
                    point.height = 'a'
                    point.visited = True
                    self.start = point
                elif height == 'E':
                    point.height = end_height
                    self.end = point
                point_row.append(point)
            self.points.append(point_row)
    
    def __repr__(self) -> str:
        out = [f'<HeightMap start={self.start} end={self.end}>']
        for row in self.points:
            out.append('\t' + ''.join([p.height for p in row]))  # heights
            # out.append('\t' + ''.join(['X' if p.visited else '.' for p in row]))  # visited
        return '\n'.join(out)


def run_bfs(height_map: HeightMap, part_2_reset=False):
    queue = [(height_map.start, 0, [])]  # Point, steps, path
    while queue:
        loc, step, path = queue.pop(0)
        if loc == height_map.end:
            return loc, step, path
        for x, y in DIRECTIONS:
            next_x = loc.x + x
            next_y = loc.y + y
            if (next_x < 0 or next_x >= len(height_map.points) or next_y < 0 or next_y >= len(height_map.points[0])):
                continue  # out of bounds; no need to check
            next = height_map.points[next_x][next_y]
            if not next.visited:
                distance = ord(next.height) - ord(loc.height)
                if distance <= 1:
                    if part_2_reset and next.height == 'a':
                        queue.insert(0, (next, 0, path + [loc]))
                    else:
                        queue.append((next, step + 1, path + [loc]))
                    next.visited = True
    raise Exception('Could not find a path to the destination!')



def solve_1(_in: str):
    height_map = HeightMap(_in)
    _, distance, path = run_bfs(height_map, False)
    return distance
    

def solve_2(_in: str):
    height_map = HeightMap(_in)
    _, distance, path = run_bfs(height_map, True)
    return distance


if __name__ == "__main__":
    with open('input/12.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')