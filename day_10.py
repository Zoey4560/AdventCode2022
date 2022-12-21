r""" Day 10

>>> sample_input = 'addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop'
>>> solve_1(sample_input)
13140
"""

class CPU:
    def __init__(self) -> None:
        self.register = 1
        self.cycle = 1
        self.next_signal_on = 20
        self.signal_increment = 40
        self.signal_strengths = []
    
    def __repr__(self) -> str:
        return f'<CPU (cycle: {self.cycle}, register: {self.register})>'

    def execute(self, command):
        if command == 'noop':
            self.next_cycle()
        else: 
            # addx num
            self.next_cycle()
            self.next_cycle()
            self.register += int(command[5:])

    def next_cycle(self):
        # check signal
        if self.cycle == self.next_signal_on:
            self.signal_strengths.append(self.register * self.cycle)
            self.next_signal_on += self.signal_increment
        # next cycle
        self.cycle += 1


def solve_1(_in):
    """Solves for signal strength"""
    cpu = CPU()
    for command in _in.split('\n'):
        cpu.execute(command)
    return sum(cpu.signal_strengths)

def solve_2(_in):
    pass


if __name__ == "__main__":
    with open('input/10.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve_1(_in)}')
        print(f'Part 2: {solve_2(_in)}')
