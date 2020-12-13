from copy import copy, deepcopy
from enum import Enum


def main():
    file = open('input.txt', 'r')

    line1 = file.readline() 
    line2 = file.readline()

    file.close()

    timestamp = int(line1)
    buses = list(map(lambda x: int(x), list(filter(lambda x: x != 'x', line2.split(',')))))

    i = timestamp
    while i <= timestamp * 2:
        for bus in buses:
            if i % bus == 0:
                wait_time = (i - timestamp) * bus
                print(wait_time)
                return
        i += 1

if __name__ == '__main__':
    main()