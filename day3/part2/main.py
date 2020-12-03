def count_trees(right, down):
    lst = []
    file1 = open('input.txt', 'r')
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(line)
    
    col = right
    row = down
    count = 0

    while row < len(lst):
        if lst[row][col] == '#':
            count = count + 1
        col = (col + right) % (len(lst[0]) - 1)
        row = row + down
    return count

def main():
    res = count_trees(3, 1) * count_trees(1, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)
    print(res)

if __name__ == "__main__":
    main()