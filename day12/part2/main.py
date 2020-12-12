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

def turn_right(degrees, waypoint_x, waypoint_y):
    if degrees == 0 or degrees == 360:
        return waypoint_x, waypoint_y
    elif degrees == 270:
        return waypoint_y, -waypoint_x
    elif degrees == 180:
        return -waypoint_x, -waypoint_y
    elif degrees == 90:
        return -waypoint_y, waypoint_x
    return waypoint_x, waypoint_y

def turn_left(degrees, waypoint_x, waypoint_y):
    return turn_right(360 - degrees, waypoint_x, waypoint_y)
    

def main():
    file = open('input.txt', 'r')
    x = 0
    y = 0

    waypoint_x = 1
    waypoint_y = 10

    while True: 
        line = file.readline() 
        if not line: 
            break
        instruction = line[0]
        value = int(line[1:])

        if instruction == north:
            waypoint_x += value
        elif instruction == south:
            waypoint_x -= value
        elif instruction == east:
            waypoint_y += value
        elif instruction == west:
            waypoint_y -= value
        elif instruction == right:
            waypoint_x, waypoint_y = turn_right(value, waypoint_x, waypoint_y)
        elif instruction == left:
            waypoint_x, waypoint_y = turn_left(value, waypoint_x, waypoint_y)
        elif instruction == forward:
            x += value * waypoint_x
            y += value * waypoint_y

    distance = abs(0 - x) + abs(0 - y)
    print(distance)

if __name__ == '__main__':
    main()