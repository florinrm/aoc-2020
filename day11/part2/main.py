from copy import copy, deepcopy

empty = 'L'
occupied = '#'
floor = '.'

def transform(lst, row, col, width, height):
    neighbour = None
    if lst[row][col] == empty:
        neighbour = occupied
    elif lst[row][col] == occupied:
        neighbour = empty

    count = 0

    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i -= 1
        j -= 1

    i = row + 1
    j = col + 1
    while i < height and j < width:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i += 1
        j += 1

    i = row - 1
    j = col + 1
    while i >= 0 and j < width:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i -= 1
        j += 1

    i = row + 1
    j = col - 1
    while i < height and j >= 0:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i += 1
        j -= 1

    i = row
    j = col - 1
    while j >= 0:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        j -= 1

    i = row
    j = col + 1
    while j < width:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        j += 1

    i = row + 1
    j = col
    while i < height:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i += 1

    i = row - 1
    j = col
    while i >= 0:
        if lst[i][j] == occupied:
            count += 1
            break
        if lst[i][j] == empty:
            break
        i -= 1

    if lst[row][col] == empty and count == 0:
        return occupied
    elif lst[row][col] == occupied and count >= 5:
        return empty
    
    return lst[row][col]

def count_occupied(lst, height, width):
    count = 0
    for i in range(height):
        for j in range(width):
            if lst[i][j] == occupied:
                count += 1
    return count

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(line.strip())

    width = len(lst[0])
    height = len(lst)

    old_lst = deepcopy(lst)

    while True:
        for i in range(height):
            for j in range(width):
                temp = list(lst[i])
                temp[j] = transform(old_lst, i, j, width, height)
                lst[i] = temp
        if old_lst == lst:
            break
        old_lst = deepcopy(lst)

    # print(("\n".join(str(item) for item in lst).replace('[', '').replace(']', '').replace(', ', '').replace('\'', '')))
    print(count_occupied(lst, height, width))

if __name__ == '__main__':
    main()