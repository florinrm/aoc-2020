from copy import copy, deepcopy

nop = 'nop'
acc = 'acc'
jmp = 'jmp'

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        data = line.split(' ')
        lst.append((data[0], int(data[1])))

    i = 0
    count = 0
    visited = set()

    while (i < len(lst)):
        if lst[i][0] == nop:
            if i in visited:
                break
            visited.add(i)
            i += 1
        elif lst[i][0] == acc:
            if i in visited:
                break
            visited.add(i)
            count += lst[i][1]
            i += 1
        elif lst[i][0] == jmp:
            if i in visited:
                break
            visited.add(i)
            i += lst[i][1]

    print(count)

if __name__ == '__main__':
    main()