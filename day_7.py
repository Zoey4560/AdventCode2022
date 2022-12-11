r""" Day 7

this one was brutal.. didn't ever have to worry about files
could have just turned the dirs into ints of their size and
just worked with them flattened... o well. recursion it is.
not sure why the _buggy_solve_2() gives the wrong answer..

>>> sample_input = '$ cd /\n$ ls\ndir a\n14848514 b.txt\n8504156 c.dat\ndir d\n$ cd a\n$ ls\ndir e\n29116 f\n2557 g\n62596 h.lst\n$ cd e\n$ ls\n584 i\n$ cd ..\n$ cd ..\n$ cd d\n$ ls\n4060174 j\n8033020 d.log\n5626152 d.ext\n7214296 k'
>>> filesystem = parse(sample_input)
>>> solve_1(filesystem)
95437
>>> solve_2(filesystem)
24933642
"""


class File:
    def __init__(self, size):
        self.size = size

    def __repr__(self):
        return f'<File: {str(self.size)}>'


class Directory(dict):
    def __init__(self, parent=None, initial={}):
        super().__init__(initial)
        self.parent = parent

    def __repr__(self):
        return f'<Dir {self.size} {super().__repr__()}>'
    
    @property
    def size(self):
        return sum([x.size for x in self.values()])


def parse(_in):
    filesystem = Directory(initial={'/': Directory()})
    current_directory = filesystem  # pointer that we'll use to navigate

    for line in _in.split('\n'):
        if line[:4] == '$ cd':
            loc = line[5:]
            if loc == '..':
                current_directory = current_directory.parent
            else:
                current_directory = current_directory[loc]

        elif line[:4] == '$ ls':
            # we're ready for it.. nothing we need to do :)
            pass

        elif line[:3] == 'dir':
            current_directory[line[4:]] = Directory(parent=current_directory)

        else:  # file
            size, name = line.split(' ')
            size = int(size)
            current_directory[name] = File(size)
    
    return filesystem


def solve_1(filesystem, max_size = 100_000):
    tally = 0
    for directory in filter(lambda x: type(x) == Directory, filesystem.values()):
        if directory.size <= max_size:
            tally += directory.size
        tally += solve_1(directory)
    return tally


def solve_2(filesystem: Directory, total=70_000_000, update=30_000_000):
    required_size = update + filesystem.size - total

    def flatten(directory):
        dirs = []
        for sub_item in directory.values():
            if type(sub_item) == Directory:
                dirs.append(sub_item.size)
                dirs += flatten(sub_item)
        return dirs

    delete_candidates = [size for size in flatten(filesystem) if size > required_size]
    return min(delete_candidates)


def _buggy_solve_2(filesystem: Directory, total=70_000_000, update=30_000_000):
    # giving the wrong answer and I don't know why... 689585
    required_size = update + filesystem.size - total
    def inner(fs, debug_offset=''):
        print(debug_offset, 'in', fs)
        smallest_file = fs
        for directory in fs.values():
            print('---', required_size)
            if type(directory) == Directory and directory.size >= required_size:

                child = inner(directory, debug_offset+'  ')
                if child.size < directory.size:
                    print(debug_offset, 'child', child)
                    smallest_file = child

                if directory.size < smallest_file.size:
                    print(debug_offset, 'dir', directory)
                    smallest_file = directory

        print(debug_offset, 's', smallest_file)
        return smallest_file
    
    file_to_delete = inner(filesystem)
    return file_to_delete.size


if __name__ == "__main__":
    with open('input/7.txt') as fh:
        _in = fh.read()
        filesystem = parse(_in)
        print(f'Part 1: {solve_1(filesystem)}')
        print(f'Part 2: {solve_2(filesystem)}')
