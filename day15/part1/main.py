from copy import copy, deepcopy
from enum import Enum
from collections import defaultdict


def main():
    file = open('input.txt', 'r')

    line = file.readline() 
    file.close()

    numbers = list(map(lambda x: int(x), line.split(',')))
    print(numbers)

    d = defaultdict(list)
    for i in range(len(numbers)):
        if numbers[i] not in d:
            d[numbers[i]] = [i]
        else:
            d[numbers[i]].append(i)

    limit = 2020

    pos = len(numbers)
    while pos < limit:
        if len(d[numbers[pos - 1]]) >= 2:
            first_pos = d[numbers[pos - 1]][-1]
            second_pos = d[numbers[pos - 1]][-2]
            numbers.append(first_pos - second_pos)
            d[first_pos - second_pos].append(pos)
        else:
            if 0 in d:
                d[0].append(pos)
            else:
                d[0] = [pos]
            numbers.append(0)
        pos += 1
    print(numbers[-1])

if __name__ == '__main__':
    main()