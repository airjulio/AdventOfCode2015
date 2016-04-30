from read_input import *


def up(current):
    return current[0], current[1] + 1


def down(current):
    return current[0], current[1] - 1


def left(current):
    return current[0] - 1, current[1]


def right(current):
    return current[0] + 1, current[1]

functions = {'^': up, 'v': down, '<': left, '>': right}


def process_santa(directions):
    map = set()
    current = (0, 0)
    map.add(current)
    for d in directions:
        current = functions.get(d)(current)
        map.add(current)
    return len(map)


def process_robot(directions):
    current_santa = (0, 0)
    current_robo = (0, 0)
    map_santa = set()
    map_robo = set()
    map_santa.add(current_santa)
    map_robo.add(current_robo)

    for i, h in enumerate(directions):
        if i % 2 == 0:
            current_santa = functions.get(h)(current_santa)
            map_santa.add(current_santa)
        else:
            current_robo = functions.get(h)(current_robo)
            map_robo.add(current_robo)

    return len(set(map_santa).union(map_robo))


if __name__ == '__main__':
    for direction in read_input():
        print(process_santa(direction))
        print(process_robot(direction))
