r""" Day 10

>>> sample_input = 'addx 15\naddx -11\naddx 6\naddx -3\naddx 5\naddx -1\naddx -8\naddx 13\naddx 4\nnoop\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx 5\naddx -1\naddx -35\naddx 1\naddx 24\naddx -19\naddx 1\naddx 16\naddx -11\nnoop\nnoop\naddx 21\naddx -15\nnoop\nnoop\naddx -3\naddx 9\naddx 1\naddx -3\naddx 8\naddx 1\naddx 5\nnoop\nnoop\nnoop\nnoop\nnoop\naddx -36\nnoop\naddx 1\naddx 7\nnoop\nnoop\nnoop\naddx 2\naddx 6\nnoop\nnoop\nnoop\nnoop\nnoop\naddx 1\nnoop\nnoop\naddx 7\naddx 1\nnoop\naddx -13\naddx 13\naddx 7\nnoop\naddx 1\naddx -33\nnoop\nnoop\nnoop\naddx 2\nnoop\nnoop\nnoop\naddx 8\nnoop\naddx -1\naddx 2\naddx 1\nnoop\naddx 17\naddx -9\naddx 1\naddx 1\naddx -3\naddx 11\nnoop\nnoop\naddx 1\nnoop\naddx 1\nnoop\nnoop\naddx -13\naddx -19\naddx 1\naddx 3\naddx 26\naddx -30\naddx 12\naddx -1\naddx 3\naddx 1\nnoop\nnoop\nnoop\naddx -9\naddx 18\naddx 1\naddx 2\nnoop\nnoop\naddx 9\nnoop\nnoop\nnoop\naddx -1\naddx 2\naddx -37\naddx 1\naddx 3\nnoop\naddx 15\naddx -21\naddx 22\naddx -6\naddx 1\nnoop\naddx 2\naddx 1\nnoop\naddx -10\nnoop\nnoop\naddx 20\naddx 1\naddx 2\naddx 2\naddx -6\naddx -11\nnoop\nnoop\nnoop'
>>> sample_device = CommsDevice()
>>> sample_device.run_input(sample_input)
>>> solve_1(sample_device)
13140
>>> solve_2(sample_device)
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

class CommsDevice:
    def __init__(self) -> None:

        # CPU
        self.register = 1
        self.cycle = 1

        # Signal Monitor
        self.next_signal_on = 20
        self.signal_increment = 40
        self.signal_strengths = []

        # CRT
        self.screen = []
        self.screen_row = []
        self.screen_width = 40
    
    def __repr__(self) -> str:
        return f'<{self.__class__} (cycle: {self.cycle}, register: {self.register})>'

    def run_input(self, _in):
        for command in _in.split('\n'):
            self.execute(command)

    def execute(self, command):
        if command == 'noop':
            self.next_cycle()
        else: 
            # addx num
            self.next_cycle()
            self.next_cycle()
            self.register += int(command[5:])

    def next_cycle(self):
        self._check_signal()
        self._render_pixel()
        self.cycle += 1

    def _check_signal(self):
        if self.cycle == self.next_signal_on:
            self.signal_strengths.append(self.register * self.cycle)
            self.next_signal_on += self.signal_increment
    
    def _render_pixel(self):
        px = '.' if abs(self.register - len(self.screen_row)) > 1 else '#'
        self.screen_row.append(px)

        # reset render row
        if len(self.screen_row) >= self.screen_width:
            self.screen.append(self.screen_row)
            self.screen_row = []
    
    def render(self):
        for row in self.screen:
            print(''.join(row))


def solve_1(device: CommsDevice):
    return sum(device.signal_strengths)

def solve_2(device: CommsDevice):
    return device.render()


if __name__ == "__main__":
    with open('input/10.txt') as fh:

        _in = fh.read()
        device = CommsDevice()
        device.run_input(_in)

        print(f'Part 1: {solve_1(device)}')

        print('Part 2:')
        solve_2(device)
