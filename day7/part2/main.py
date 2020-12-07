from copy import copy, deepcopy

shiny = 'shiny gold'

def search_shiny(d, bag):
    if bag == shiny:
        return True

    dic = deepcopy(d)
    
    if not dic[bag]:
        return False

    res = False
    for (b, k) in dic[bag].items():
        if k != []:
            res = res or (search_shiny(deepcopy(dic), b))
    
    return res

def count_shiny(d, bag):
    dic = deepcopy(d)
    
    if not dic[bag]:
        return 1
    
    count = 1
    for (b, k) in dic[bag].items():
        if k != []:
            count = count + k * (count_shiny(deepcopy(dic), b))
    
    return count

def main():
    file1 = open('input.txt', 'r')
    lst = []
    bags = dict()
    while True: 
        line = file1.readline() 
        if not line: 
            break
        
        words = line.split(' ')
        bag_type = words[0] + " " + words[1]
        sub_bags = []
        
        if words[4] == 'no' and words[5] == 'other':
            bags[bag_type] = {}
        else:
            i = 4
            bag_dict = dict()
            while i < len(words):
                n = int(words[i])
                sub_bag_type = words[i + 1] + " " + words[i + 2]
                bag_dict[sub_bag_type] = n
                i += 4
            bags[bag_type] = bag_dict

    print(count_shiny(deepcopy(bags), shiny) - 1)
    
if __name__ == '__main__':
    main()