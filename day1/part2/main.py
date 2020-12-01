def main():
    file1 = open('input.txt', 'r')
    numbers = dict()
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        numbers[int(line)] = int(line)
        lst.append(int(line))

    for e in lst:
        for p in lst:
            if (2020 - e - p) in numbers:
                if e != p and e != (2020 - e - p) and p != (2020 - e - p):
                    result = p * e * (2020 - e - p)
                    print(result)
                    return

if __name__ == "__main__":
    main()