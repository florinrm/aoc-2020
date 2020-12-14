from copy import copy, deepcopy
from enum import Enum

def to_binary(n):
    return format(n, 'b').zfill(36)

def to_int(bin):
    return int(bin, 2)

def main():
    file = open('input.txt', 'r')
    addresses = dict()

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
            binary = to_binary(val)
            for i in range(len(mask)):
                if mask[i] == 'X':
                    res.append(binary[i])
                    continue
                if mask[i] != binary[i]:
                    res.append(mask[i])
                else:
                    res.append(binary[i])
            addresses[dic_key] = to_int("".join(res))
    s = 0
    for _, v in addresses.items():
        s += v
    print(s)

if __name__ == '__main__':
    main()