def main():
    lst = []
    file1 = open('input.txt', 'r')
    info_dict = dict()
    while True: 
        line = file1.readline() 
        if not line: 
            break
        if len(line) == 1:
            lst.append(info_dict)
            info_dict = dict()

        data = line.split(" ")
        for info in data:
            pair = info.strip().split(":")
            if len(pair) == 2:
                info_dict[pair[0]] = pair[1]

    lst.append(info_dict)   

    count = 0
    for elem in lst:
        if len(elem) == 7 and 'cid' not in elem:
            count += 1
        if len(elem) == 8:
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()
    