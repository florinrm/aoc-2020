from copy import copy, deepcopy
from enum import Enum
from functools import reduce

# code stolen from rosettacode.org
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
 
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
 
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

def main():
    file = open('input.txt', 'r')

    line1 = file.readline() 
    line2 = file.readline()

    file.close()

    timestamp = int(line1)
    # buses = list(map(lambda x: int(x), list(filter(lambda x: x != 'x', line2.split(',')))))

    data = line2.split(',')
    pos = []
    buses = []
    for i in range(len(data)):
        if data[i] != 'x':
            pos.append(-i)
            buses.append(int(data[i]))

    print(chinese_remainder(buses, pos))

if __name__ == '__main__':
    main()