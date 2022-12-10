""" Day 6

>>> sample_input = 'mjqjpqmgbljsphdztnvjfqwrcgsmlb'
>>> solve(sample_input, 4)
7
>>> solve(sample_input, 14)
19
"""


def solve(_in, scan_size):
    i = scan_size
    while _in:
        if len(set(_in[:scan_size])) == scan_size:
            return i
        _in = _in[1:]
        i += 1


if __name__ == "__main__":
    with open('input/6.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve(_in, 4)}')
        print(f'Part 2: {solve(_in, 14)}')
