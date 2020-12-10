from copy import copy, deepcopy

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(int(line))

    max_elem = max(lst)
    lst.append(0)
    lst.append(max_elem + 3)
    lst = sorted(lst)

    arrangements = [0] * len(lst)
    arrangements[0] = 1

    for i in range(1, len(lst)):
        for j in range(i - 1, -1, -1):
            if lst[i] - lst[j] <= 3:
                arrangements[i] += arrangements[j]
            else:
                break
    
    print(arrangements[-1])

if __name__ == '__main__':
    main()