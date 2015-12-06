INPUT_FILE = '../input.txt'


def read_input(input_file=INPUT_FILE):
    with open(input_file) as f:
        for line in f:
            yield line.strip()
