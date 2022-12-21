r""" Day 11

>>> sample_input = 'Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1'
>>> solve_1(sample_input)
10605



"""



class Monkey:
    items = []
    operation = None
    test = None
    true_throw = None
    false_throw = None

    def __init__(self, _monkey_string: str):
        _, item_str, op_str, *test_strs = _monkey_string.split('\n')
        print(item_str)
        print(op_str)
        print(test_strs)



def solve_1(_in):
    monkeys = []
    for monkey_string in _in.split('\n\n'):
        return Monkey(monkey_string)


def solve_2(_in):
    pass





if __name__ == "__main__":
    with open('input/11.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')