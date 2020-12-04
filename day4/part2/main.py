def is_valid(d):
    res = False
    if len(d) == 7 and 'cid' not in d:
        res = True
    if len(d) == 8:
        res = True
    return res

def is_byr_valid(d):
    byr = d['byr']
    n = int(byr)
    return 1920 <= n and n <= 2002

def is_iyr_valid(d):
    iyr = d['iyr']
    n = int(iyr)
    return 2010 <= n and n <= 2020

def is_eyr_valid(d):
    eyr = d['eyr']
    n = int(eyr)
    return 2020 <= n and n <= 2030

def is_hgt_valid(d):
    hgt = d['hgt']
    
    if 'cm' not in hgt and 'in' not in hgt:
        return False
    
    if 'cm' in hgt:
        cm = int(hgt[:-2])
        return 150 <= cm and cm <= 193
    else:
        n = int(hgt[:-2])
        return 59 <= n <= 76
    
def is_hcl_valid(d):
    hcl = d['hcl']
    
    if hcl[0] != '#':
        return False
    
    res = hcl[1:]
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0',
        'a', 'b', 'c', 'd', 'e', 'f']

    for l in res:
        if l not in lst:
            return False
    
    return True

def is_ecl_valid(d):
    ecl = d['ecl']
    lst = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    return (ecl in lst)

def is_pid_valid(d):
    pid = d['pid']
    lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    if len(pid) != 9:
        return False

    for p in pid:
        if p not in lst:
            return False

    return True

def is_completely_valid(d):
    return (is_valid(d) 
        and is_byr_valid(d)
        and is_ecl_valid(d)
        and is_eyr_valid(d)
        and is_hcl_valid(d)
        and is_hgt_valid(d)
        and is_iyr_valid(d)
        and is_pid_valid(d))

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
        if is_completely_valid(elem):
            count += 1
    
    print(count)

if __name__ == '__main__':
    main()
    