def main():
    file1 = open('input.txt', 'r')
    count = 0
    while True: 
        line = file1.readline() 
        if not line: 
            break
        tokens = line.split(" ")

        positions = tokens[0].split("-")
        first_pos = int(positions[0])
        second_pos = int(positions[1])

        letter = tokens[1][:-1]

        string = tokens[2]

        is_valid = False

        if first_pos <= len(string):
            if letter == string[first_pos - 1]:
                is_valid = True 

        if second_pos <= len(string):
            if letter == string[second_pos - 1]:
                if is_valid == True:
                    is_valid = False
                else:
                    is_valid = True 

        if is_valid == True:
            count = count + 1

    print(count)

if __name__ == "__main__":
    main()