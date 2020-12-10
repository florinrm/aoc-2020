from copy import copy, deepcopy

def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(int(line))

    max_elem = max(lst)
    lst.append(0)
    lst.append(max_elem + 3)
    lst = sorted(lst)

    count_one_diff = 0
    count_three_diff = 0

    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] == 1:
            count_one_diff += 1
        if lst[i + 1] - lst[i] == 3:
            count_three_diff += 1
    
    result = count_one_diff * count_three_diff
    print(result)

if __name__ == '__main__':
    main()