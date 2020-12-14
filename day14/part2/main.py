from copy import copy, deepcopy
from enum import Enum
from itertools import combinations

def to_binary(n):
    return format(n, 'b').zfill(36)

def to_int(bin):
    return int(bin, 2)

def generate(n):
    return list(set(list(combinations([0, 1] * 2 * n, n))))

addresses = dict()

def make_combinations(res, combs):
    lsts = []
    for c in combs:
        temp = []
        pos = 0
        for r in res:
            if r == 'X':
                temp.append(str(c[pos]))
                pos += 1
            else:
                temp.append(r)
        lsts.append(temp)
    return lsts

def main():
    file = open('input.txt', 'r')

    mask = None
    while True: 
        line = file.readline() 
        if not line: 
            break
        line = line.strip()
        data = line.split(" ")
        if data[0] == 'mask':
            mask = data[2]
        else:
            val_str = data[0]
            val_str = val_str[:-1]

            dic_key = int(val_str[4:])
            val = int(data[2])

            res = []
            binary = to_binary(dic_key)
            for i in range(len(mask)):
                if mask[i] == 'X':
                    res.append(mask[i])
                elif mask[i] == '1':
                    res.append(mask[i])
                else:
                    res.append(binary[i])
            # print(''.join(res))

            count_x = len(list(filter(lambda x: x == 'X', res)))
            numbers = list(map(lambda x: to_int(x), list(map(lambda x: ''.join(x), make_combinations(res, generate(count_x))))))

            print(mask)
            print(numbers)
            print("")

            for n in numbers:
                addresses[n] = val

    s = 0
    for _, v in addresses.items():
        s += v
    print(s)

if __name__ == '__main__':
    main()