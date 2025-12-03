from itertools import combinations

def maximum(bank):
    maxim = 0
    current_num = 0
    index1 = 0
    print(bank)

    while index1 < len(bank) - 1:
        index2 = index1 + 1

        while index2 < len(bank) - 1:
            current_num = int(bank[index1]) * 10 + int(bank[index2])
            print(current_num)
            if current_num > maxim:
                maxim = current_num
            index2 += 1

        index1 += 1

    return maxim

def generate_number(index_list, bank):
    number = 0
    ten = pow(10,11)
    comb_index = 0
    while comb_index < 12:
        index_used = index_list[comb_index]
        number = number + (int(bank[index_used]) * ten)
        comb_index+=1
        ten//=10
    return number

def maximum2(bank):
    index_list = []
    
    for _ in range (0,len(bank)):
        index_list.append(_)
    print(bank)
    print(index_list)
    comb = combinations(index_list, 12)
    max = 0
    current_num = 0
    for i in comb:
        current_num = generate_number(i, bank)
        if current_num > max:
            max = current_num
        

    return max




def solve():
    file = open("input.txt", "r")
    bank = file.readline()
    sum = 0
    
    while bank:

        bank = list(bank.strip())
        
        add = maximum2(bank)    
        print(add)

        sum += add
        bank = file.readline()
    
    print(sum)

solve()