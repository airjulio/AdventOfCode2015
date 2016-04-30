from read_input import *

UP = '('
DOWN = ')'


if __name__ == '__main__':
    for item in read_input('../input.txt'):
        print(item.count(UP) - item.count(DOWN))
