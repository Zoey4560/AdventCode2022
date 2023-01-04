r""" Day 11

>>> sample_input = 'Monkey 0:\n  Starting items: 79, 98\n  Operation: new = old * 19\n  Test: divisible by 23\n    If true: throw to monkey 2\n    If false: throw to monkey 3\n\nMonkey 1:\n  Starting items: 54, 65, 75, 74\n  Operation: new = old + 6\n  Test: divisible by 19\n    If true: throw to monkey 2\n    If false: throw to monkey 0\n\nMonkey 2:\n  Starting items: 79, 60, 97\n  Operation: new = old * old\n  Test: divisible by 13\n    If true: throw to monkey 1\n    If false: throw to monkey 3\n\nMonkey 3:\n  Starting items: 74\n  Operation: new = old + 3\n  Test: divisible by 17\n    If true: throw to monkey 0\n    If false: throw to monkey 1'
>>> solve_1(sample_input)
10605
>>> solve_2(sample_input)
2713310158

"""
from typing import List
from enum import auto, Enum
from math import prod

class MonkeyType(Enum):
    ADD = auto()
    MULT = auto()
    SQ = auto()



class Monkey:

    items: List[int]
    monkey_type: MonkeyType
    operation = None
    test: int
    true_throw: int
    false_throw: int
    inspection_count: int = 0
    relief = None

    def __repr__(self) -> str:
        return f'<Monkey {self.items}>'

    def __init__(self, _monkey_string: str, simple_relief=True):
        _, item_str, op_str, *test_strs = _monkey_string.split('\n')

        self.items = [int(item) for item in item_str[18:].split(', ')]

        self.monkey_type, self.operation = self._get_monkey_type_and_op(op_str)

        self.test = int(test_strs[0][21:])
        self.true_throw = int(test_strs[1][29:])
        self.false_throw = int(test_strs[2][30:])

        if simple_relief:
            self.relief = lambda x: x // 3
        else:
            self.relief = None  # Note: Patched in, once we know all the other monkeys

    def throw_items(self):
        for item in self.items:
            item = self.operation(item)
            self.inspection_count += 1
            item = self.relief(item)
            target = self.true_throw if item % self.test == 0 else self.false_throw
            yield target, item
        self.items = []


    @staticmethod
    def _get_monkey_type_and_op(op_str):
        if op_str[25:] == 'old':  # assumes that there's only `old * old` and not `old + old`
            return MonkeyType.SQ, lambda x: pow(x, 2)
        else:
            factor = int(op_str[25:])
            if op_str[23] == '+':
                return MonkeyType.ADD, lambda x: x + factor
            else: # == '*'
                return MonkeyType.MULT, lambda x: x * factor




def solve(_in, rounds, simple_relief):
    monkeys = []
    for monkey_string in _in.split('\n\n'):
        monkeys.append(Monkey(monkey_string))

    if not simple_relief:
        tests = [m.test for m in monkeys]
        common_factor = prod(tests)
        r = lambda x: x % common_factor
        for monkey in monkeys:
            monkey.relief = r

    for r in range(rounds):
        # play rounds
        for monkey in monkeys:
            for target, item in monkey.throw_items():
                monkeys[target].items.append(item)
    
    inspection_counts = [m.inspection_count for m in monkeys]
    inspection_counts.sort(reverse=True)
    return inspection_counts[0] * inspection_counts[1]

def solve_1(_in):
    return solve(_in, 20, True)
    

def solve_2(_in):
    return solve(_in, 10_000, False)


if __name__ == "__main__":
    with open('input/11.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')