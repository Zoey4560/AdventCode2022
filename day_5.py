r""" Day 5

    [D]    
[N] [C]    
[Z] [M] [P]
 1   2   3 

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2

>>> sample_input = '    [D]    \n[N] [C]    \n[Z] [M] [P]\n 1   2   3 \n\nmove 1 from 2 to 1\nmove 3 from 1 to 3\nmove 2 from 2 to 1\nmove 1 from 1 to 2'
>>> solve(sample_input, cratemover_9000_logic)
'CMZ'
>>> solve(sample_input, cratemover_9001_logic)
'MCD'

"""

import re


move_matching = 'move (\d+) from (\d+) to (\d)'


def cratemover_9000_logic(stacks, count, source, dest):
    for _ in range(int(count)):
            stacks[dest].append(stacks[source].pop())


def cratemover_9001_logic(stacks, count, source, dest):
    stacks[source], grabbed = stacks[source][:-count], stacks[source][-count:]
    stacks[dest] += grabbed
    


def solve(_in, versioned_logic):
    raw_stacks, raw_commands = [x.split('\n') for x in _in.split('\n\n')]

    # parse the stacks
    stacks = []  # uses zero based index (not 1)
    *stacks_data, stack_numbers = [list(x) for x in raw_stacks]
    for num in stack_numbers:        
        column = [x.pop(0) for x in stacks_data]  # strip off the front
        if num == ' ':
            continue  # skip blank columns
        # clean up column and store in stacks
        column = [x for x in column if x  != ' ']
        column.reverse()
        stacks.append(column)

    # move crates
    for raw_command in raw_commands:
        count, *sd = [int(x) for x in re.match(move_matching, raw_command).groups()]
        source, dest = [x - 1 for x in sd]  # convert to zero based index

        # mutate stacks based on 9000 or 9001 logic
        versioned_logic(stacks, count, source, dest)

    return ''.join(x.pop() for x in stacks)
    

if __name__ == "__main__":
    with open('input/5.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {solve(_in, cratemover_9000_logic)}')
        print(f'Part 1: {solve(_in, cratemover_9001_logic)}')