r""" Day 8

>>> sample_input = '30373\n25512\n65332\n33549\n35390'
>>> solve_1(sample_input)
21
>>> solve_2(sample_input)
8

"""


def parse(_in):
    trees = []
    for row in _in.split('\n'):
        trees.append([int(x) for x in row])
    return trees


def solve_1(_in):
    count = 0
    trees = parse(_in)

    # for each of the inner trees
    for i in range(1, len(trees) - 1):
        for j in range(1, len(trees[0]) - 1):
            tree = trees[i][j]

            left  = trees[i][:j]
            right = trees[i][j+1:]
            up   = [x[j] for x in trees[:i]]
            down = [x[j] for x in trees[i+1:]]

            lowest_potential_blocker = min([max(x) for x in [left, right, up, down] ])
            if tree > lowest_potential_blocker:
                count += 1
    # visible inner trees + outside rows + outside columns - double counted corners
    return count + (len(trees) * 2) + (len(trees[0]) * 2) - 4


def apraise(tree, view):
    """ Looks in one direction; counting how many trees can be seen
    >>> apraise(3, [1, 2, 3, 4])
    3
    >>> apraise(3, [2, 5])
    2
    >>> apraise(5, [2])
    1
    >>> apraise(3, [])
    0
    """
    count = 0
    for t in view:
        count += 1
        if t >= tree:
            return count
    return count
    

def solve_2(_in):
    # there's probably something clever to do that could figure out
    # which trees are good candidates; instad of scoring every one.
    #   likely to be a high height tree to begin with
    # but; it runs instantly anyways -- in human time.
    best_view = 0
    trees = parse(_in)

    for i, row in enumerate(trees):
        for j, tree in enumerate(row):

            left  = apraise(tree, reversed(trees[i][:j]))
            right = apraise(tree, trees[i][j+1:])
            up    = apraise(tree, reversed([x[j] for x in trees[:i]]))
            down  = apraise(tree, [x[j] for x in trees[i+1:]] )

            view = left * right * up * down

            if view > best_view:
                best_view = view

    return best_view


if __name__ == "__main__":
    with open('input/8.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')