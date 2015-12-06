from read_input import *


def calculate_paper(box):
    lw = box.length * box.width
    wh = box.width * box.height
    hl = box.height * box.length
    area = (2 * lw) + (2 * wh) + (2 * hl)
    smallest_side = min([lw, wh, hl])
    return area + smallest_side

if __name__ == '__main__':
    total = 0
    for box_dimension in read_input():
        total += calculate_paper(box_dimension)
    print(total)