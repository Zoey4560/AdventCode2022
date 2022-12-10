r""" Day 3
>>> sample_in = 'vJrwpWtwJgWrhcsFMMfFFhFp\njqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL\nPmmdzqPrVvPwwTWBwg\nwMqvLMZHhHMvwLHjbvcjnnSBnvTQFn\nttgJtRGJQctTZtZT\nCrZsJsPPZsGzwwsLwLmpwMDw'
>>> part_1(sample_in)
157
>>> part_2(sample_in)
70
"""


def parse_split(_in):
    raw_sacks = _in.split('\n')
    rucksacks = []
    for sack in raw_sacks:
        l = len(sack)//2
        rucksacks.append((sack[:l], sack[l:]))
    return rucksacks


def parse_chunked(_in):
    raw_sacks = _in.split('\n')
    groups = []
    for i in range(0, len(raw_sacks), 3):
        groups.append(raw_sacks[i:i+3])
    return groups


def find_shared_item(sack):
    for item in sack[0]:
        if item in sack[1]:
            # Assumes that there's only ever one shared item.
            return item


def find_badge(group):
    for sack in group:
        for item in sack:
            if all(item in _sack for _sack in group):
                # double checks it's own list; could probably optimize that but...
                return item
    raise Exception(f"Badge not found for group: {group}")


def priority(item):
    if item == item.lower():
        return ord(item) - 96   # ord('a') => 97
    return ord(item) - 65 + 27  # ord('A') => 65


def part_1(_in):
    rucksacks = parse_split(_in)
    return sum(priority(find_shared_item(sack)) for sack in rucksacks)


def part_2(_in):
    groups = parse_chunked(_in)
    return sum(priority(find_badge(group)) for group in groups)


if __name__ == "__main__":
    with open('input/3.txt') as fh:
        _in = fh.read()
        print(f'Part 1: {part_1(_in)}')
        print(f'Part 2: {part_2(_in)}')
