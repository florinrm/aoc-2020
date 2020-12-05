def decrypt(code):
    row = code[:7]
    col = code[7:]

    start = 0
    end = 127
    step = 64

    row_index = 0
    col_index = 0

    for r in range(len(row)):
        if row[r] == 'F':
            end = end - step
        elif row[r] == 'B':
            start = start + step
        step = step / 2
        if r == len(row) - 1:
            if row[r] == 'F':
                row_index = end
            else:
                row_index = start

    start = 0
    end = 7
    step = 4

    for c in range(len(col)):
        if col[c] == 'R':
            start = start + step
        elif col[c] == 'L':
            end = end - step

        step = step / 2

        if c == len(col) - 1:
            if col[c] == 'R':
                col_index = end
            else:
                col_index = start

    row_index = int(row_index)
    col_index = int(col_index)
    res = row_index * 8 + col_index
    return res

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(decrypt(line))
    
    min_list = min(lst)
    max_list = max(lst)
    temp = list(range(min_list, max_list + 1))

    for elem in temp:
        if elem not in lst:
            print(elem)
            break

if __name__ == '__main__':
    main()
    