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
        if (2020 - e) in numbers:
            result = e * (2020 - e)
            print(result)
            return

if __name__ == "__main__":
    main()