from copy import copy, deepcopy

def generate(rng, lst, index):
    start = index - rng
    end = index
    res = []

    for i in range(start, end - 1):
        for j in range(i + 1, end):
            res.append((lst[i], lst[j]))

    return res

def find_first(rng, lst):
    start_index = rng
    while start_index < len(lst):
        pairs = generate(rng, lst, start_index)
        ok = False
        for (a, b) in pairs:
            if lst[start_index] == (a + b):
                ok = True
                break
        if ok == False:
            return (lst[start_index], start_index)
        start_index += 1
    
    return None

def find_sub_list_sum(lst, element):
    curr_sum = 0
    for i in range(len(lst) - 1):
        curr_sum = lst[i]
        for j in range(i + 1, len(lst)):
            if curr_sum == element:
                return (i, j - 1)
            if curr_sum > element:
                break
            curr_sum += lst[j]
    return None


def main():
    file1 = open('input.txt', 'r')
    lst = []
    while True: 
        line = file1.readline() 
        if not line: 
            break
        lst.append(int(line))

    rng = 25
    element, _ = find_first(rng, lst)
    start, end = find_sub_list_sum(lst, element)
    
    temp = lst[start : (end + 1)]
    res = max(temp) + min(temp)
    print(res)

if __name__ == '__main__':
    main()