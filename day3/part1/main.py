def main():
    lst = []
    file1 = open('input.txt', 'r')
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(line)
    
    col = 3
    row = 1
    count = 0

    while row < len(lst):
        if lst[row][col] == '#':
            count = count + 1
        col = (col + 3) % (len(lst[0]) - 1)
        row = row + 1
        
    print(count)

if __name__ == "__main__":
    main()