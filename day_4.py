r"""" DAY 4

>>> sample_in = '2-4,6-8\n2-3,4-5\n5-7,7-9\n2-8,3-7\n6-6,4-6\n2-6,4-8'
>>> solver(sample_in, part_1_rule)
2
>>> solver(sample_in, part_2_rule)
4

"""

part_1_rule = lambda l_low, l_high, r_low, r_high: l_low <= r_low and l_high >= r_high or l_low >= r_low and l_high <= r_high
part_2_rule = lambda l_low, l_high, r_low, r_high: not (l_low > r_high or r_low > l_high)

def solver(_in, counting_rule):
    count = 0
    for pair in _in.split('\n'):
        l, r = pair.split(',')
        l_low, l_high = map(int, l.split('-'))
        r_low, r_high = map(int, r.split('-'))
        if counting_rule(l_low, l_high, r_low, r_high):
            count += 1
    return count


if __name__ == "__main__":
    with open('input/4.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solver(_in, part_1_rule)}')
        print(f'Part 2: {solver(_in, part_2_rule)}')