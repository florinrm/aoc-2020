def main():
    file1 = open('input.txt', 'r')
    lst = []
    choices = set()
    while True: 
        line = file1.readline() 
        if not line: 
            break
        if line == '\n':
            lst.append(choices)
            choices = set()
            continue
        if len(line) > 1:
            for letter in line:
                if letter != '\n':
                    choices.add(letter)
        elif len(line) == 1:
            choices.add(line)

    lst.append(choices)
    count = 0
    for e in lst:
        count += len(e)
    print(count)

if __name__ == '__main__':
    main()