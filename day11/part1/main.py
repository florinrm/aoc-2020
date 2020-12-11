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

    if row - 1 >= 0 and col - 1 >= 0:
        if lst[row - 1][col - 1] == occupied:
            count += 1
    
    if row - 1 >= 0 and col + 1 < width:
        if lst[row - 1][col + 1] == occupied:
            count += 1

    if row + 1 < height and col - 1 >= 0:
        if lst[row + 1][col - 1] == occupied:
            count += 1

    if row + 1 < height and col + 1 < width:
        if lst[row + 1][col + 1] == occupied:
            count += 1

    if col - 1 >= 0:
        if lst[row][col - 1] == occupied:
            count += 1
    
    if col + 1 < width:
        if lst[row][col + 1] == occupied:
            count += 1

    if row + 1 < height:
        if lst[row + 1][col] == occupied:
            count += 1

    if row - 1 >= 0:
        if lst[row - 1][col] == occupied:
            count += 1

    if lst[row][col] == empty and count == 0:
        return occupied
    elif lst[row][col] == occupied and count >= 4:
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