from copy import copy, deepcopy

nop = 'nop'
acc = 'acc'
jmp = 'jmp'

def has_cycle(lst):
    i = 0
    visited = set()

    while (i < len(lst)):
        if lst[i][0] == nop:
            if i in visited:
                return True
            visited.add(i)
            i += 1
        elif lst[i][0] == acc:
            if i in visited:
                return True
            visited.add(i)
            i += 1
        elif lst[i][0] == jmp:
            if i in visited:
                return True
            visited.add(i)
            i += lst[i][1]
    
    return False

def check_jumps_and_nops(lst):
    indexes = []
    for i in range(len(lst)):
        if lst[i][0] == jmp or lst[i][0] == nop:
            indexes.append(i)

    return indexes

def generate(lst):
    lists = []
    indexes = check_jumps_and_nops(lst)

    for index in indexes:
        copy_lst = deepcopy(lst)
        if copy_lst[index][0] == jmp:
            copy_lst[index] = (nop, copy_lst[index][1])
        elif copy_lst[index][0] == nop:
            copy_lst[index] = (jmp, copy_lst[index][1])
        lists.append(copy_lst)

    for l in lists:
        if has_cycle(l) == False:
            return l
    
    return []


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

    lst = generate(lst)
    
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