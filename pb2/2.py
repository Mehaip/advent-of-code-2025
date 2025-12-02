def divizorii_unui_numar(nr):
    lista_div = []

    for i in range(1,nr//2+1):
        if nr % i == 0:
            lista_div.append(i)
    return lista_div


def digits_repeat(number):
    number = str(number)
    number_length = len(number)
    lista_divizori = divizorii_unui_numar(number_length)

    for token_size in lista_divizori:
        print(f"Token size = ", token_size)
        token_end_index = token_size
        print(f"Token end index = ", token_end_index)
        first_token = number[:token_end_index]
        print(f"first_token = ", first_token)
        valid_number = True
        while token_end_index <= int(number_length):

            if first_token != number[token_end_index - token_size: token_end_index]:
                valid_number = False
            token_end_index += token_size
        
        if valid_number == True:
            return True

    return False





def solve():
    file = open("input.txt", "r")
    input = file.readline()
    sum = 0
    input = input.split(",")

    for id_ranges in input:
        id_ranges = id_ranges.split("-")
        for number in range(int(id_ranges[0]), int(id_ranges[1]) + 1):
            if digits_repeat(number):
                sum += number
    print(sum)

solve()



