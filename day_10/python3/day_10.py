import sys


def parse(input):
    parsed = []
    prev = input[0]
    parsed.append([prev])
    for c in input[1:]:
        if c == prev:
            parsed[-1].append(c)
        else:
            parsed.append([c])
        prev = c
    return parsed


def generate(parsed):
    result = ''
    for l in parsed:
        result += '{}{}'.format(len(l), l[0])
    return result


if __name__ == '__main__':
    f = sys.argv[1]
    n = sys.argv[2]
    for i in range(int(n)):
        f = generate(parse(f))
    print(len(f))
