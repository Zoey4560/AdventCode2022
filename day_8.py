r""" Day 8

>>> sample_input = '30373\n25512\n65332\n33549\n35390'
>>> solve_1(sample_input)
21
>>> solve_2(sample_input)
8

"""


def parse(_in):
    buildings = []
    for row in _in.split('\n'):
        buildings.append([int(x) for x in row])
    return buildings


def solve_1(_in):
    buildings = parse(_in)
    count = 0
    # for each of the inner buildings
    for i in range(1, len(buildings) - 1):
        for j in range(1, len(buildings[0]) - 1):
            b = buildings[i][j]
            row_left = buildings[i][:j]
            row_right = buildings[i][j+1:]
            column_above = [x[j] for x in buildings[:i]]
            column_below =  [x[j] for x in buildings[i+1:]]
            lowest_potential_blocker = min([max(x) for x in [row_left, row_right, column_above, column_below] ])
            if b > lowest_potential_blocker:
                count += 1
    # visible inner trees + outside rows + outside columns - double counted corners
    return count + (len(buildings) * 2) + (len(buildings[0]) * 2) - 4

def solve_2(_in):
    pass
        


if __name__ == "__main__":
    with open('input/8.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')