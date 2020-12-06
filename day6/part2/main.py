def main():
    file1 = open('input.txt', 'r')
    lst = []
    group_lst = []
    line_count = 0
    while True: 
        line = file1.readline() 
        if not line: 
            break
        if line == '\n':
            lst.append(group_lst)
            group_lst = []
            continue
        group_lst.append(set(list(line.strip())))
    lst.append(group_lst)
    
    count = 0
    for l in lst:
        count += len(set.intersection(*l))
    print(count)
    
if __name__ == '__main__':
    main()