from codecs import open


def read_input(input_file):
    with open(input_file) as f:
        moves = list()
        for line in f:
            moves.append([char for char in line])
    return moves


if __name__ == '__main__':
    moves = read_input('../input.txt')
    for item in moves:
        print(item.count('(') - item.count(')'))
