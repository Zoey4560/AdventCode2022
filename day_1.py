def count_calories(_in):
    return max([ sum([int(food) for food in elf.split('\n')]) for elf in _in.split('\n\n') ])

def top_three(_in):
    return sum(sorted(
            [ sum([int(food) for food in elf.split('\n')]) for elf in _in.split('\n\n') ],
            reverse=True
        )[:3])

