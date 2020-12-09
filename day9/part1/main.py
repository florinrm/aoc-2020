from copy import copy, deepcopy

def generate(rng, lst, index):
    start = index - rng
    end = index
    res = []

    for i in range(start, end - 1):
        for j in range(i + 1, end):
            res.append((lst[i], lst[j]))

    return res

def find_first(rng, lst):
    start_index = rng
    while start_index < len(lst):
        pairs = generate(rng, lst, start_index)

        ok = False
        for (a, b) in pairs:
            if lst[start_index] == (a + b):
                ok = True
                break
        if ok == False:
            print(lst[start_index])
            return

        start_index += 1
    print('Nothing')

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(int(line))

    rng = 5
    find_first(rng, lst)

if __name__ == '__main__':
    main()