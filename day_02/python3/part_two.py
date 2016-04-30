from read_input import *


def calculate_ribbon(box):
    sorted_dimensions = sorted(box)
    d1 = sorted_dimensions[0] * 2
    d2 = sorted_dimensions[1] * 2
    return d1 + d2 + (box.length * box.width * box.height)

if __name__ == '__main__':
    total = 0
    for box_dimension in read_input():
        total += calculate_ribbon(box_dimension)
    print(total)