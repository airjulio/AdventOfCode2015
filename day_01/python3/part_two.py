from read_input import *

UP = '('
DOWN = ')'


def process(m):
    position = 1
    for i in range(len(m)):
        if m[i] == UP:
            position += 1
        elif m[i] == DOWN:
            position -= 1
        if position == -1:
            return i


if __name__ == '__main__':
    for item in read_input('../input.txt'):
        print(process(item))
