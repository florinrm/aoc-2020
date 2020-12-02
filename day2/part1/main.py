def main():
    file1 = open('input.txt', 'r')
    count = 0
    while True: 
        line = file1.readline() 
        if not line: 
            break
        tokens = line.split(" ")

        max_min = tokens[0].split("-")
        min_count = int(max_min[0])
        max_count = int(max_min[1])

        letter = tokens[1][:-1]

        string = tokens[2]
        countLetter = string.count(letter)
        if countLetter >= min_count and countLetter <= max_count:
            count = count + 1

    print(count)
if __name__ == "__main__":
    main()