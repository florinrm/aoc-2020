from copy import copy, deepcopy
from enum import Enum

class Direction(Enum):
    EAST = 'east'
    WEST = 'west'
    NORTH = 'north'
    SOUTH = 'south'

north = 'N'
south = 'S'
east = 'E'
west = 'W'
forward = 'F'
right = 'R'
left = 'L'

def turn_right(direction, degrees):
    if degrees == 0 or degrees == 360:
        return direction
    elif degrees == 90:
        if direction == Direction.EAST:
            return Direction.SOUTH
        elif direction == Direction.SOUTH:
            return Direction.WEST
        elif direction == Direction.WEST:
            return Direction.NORTH
        elif direction == Direction.NORTH:
            return Direction.EAST
    elif degrees == 180:
        if direction == Direction.EAST:
            return Direction.WEST
        elif direction == Direction.SOUTH:
            return Direction.NORTH
        elif direction == Direction.WEST:
            return Direction.EAST
        elif direction == Direction.NORTH:
            return Direction.SOUTH
    elif degrees == 270:
        if direction == Direction.EAST:
            return Direction.NORTH
        elif direction == Direction.SOUTH:
            return Direction.EAST
        elif direction == Direction.WEST:
            return Direction.SOUTH
        elif direction == Direction.NORTH:
            return Direction.WEST
    return direction

def turn_left(direction, degrees):
    return turn_right(direction, 360 - degrees)
    

def main():
    file = open('input.txt', 'r')
    direction = Direction.EAST
    x = 0
    y = 0

    while True: 
        line = file.readline() 
        if not line: 
            break
        instruction = line[0]
        value = int(line[1:])

        if instruction == north:
            x += value
        elif instruction == south:
            x -= value
        elif instruction == east:
            y += value
        elif instruction == west:
            y -= value
        elif instruction == right:
            direction = turn_right(direction, value)
        elif instruction == left:
            direction = turn_left(direction, value)
        elif instruction == forward:
            if direction == Direction.NORTH:
                x += value
            elif direction == Direction.SOUTH:
                x -= value
            elif direction == Direction.EAST:
                y += value
            elif direction == Direction.WEST:
                y -= value

    distance = abs(0 - x) + abs(0 - y)
    print(distance)

if __name__ == '__main__':
    main()