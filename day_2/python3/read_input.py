from collections import namedtuple

Box = namedtuple('Box', ['length', 'width', 'height'])
INPUT_FILE = '../input.txt'


def read_input(input_file=INPUT_FILE):
    with open(input_file) as f:
        for line in f:
            l, w, h = [int(x) for x in line.split('x')]
            yield Box(l, w, h)
