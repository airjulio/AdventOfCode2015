def read_input(input_file):
    with open(input_file) as f:
        for line in f:
            yield [char for char in line]
