def solve():
    file = open("input1.txt", "r")
    file_out = open("output1.csv", "w")
    line = file.readline()
    password = 0
    scor = 50
    file_out.write("Miscare,Scor,Password\n")
    file_out.write("-,50,0\n")
    while line:
        shift_direction = line[0]
        shift_number2 = (int)(line[1:])
        password = password + (shift_number2 // 100)
        shift_number = shift_number2 % 100
        if shift_direction == 'L':
            if scor == 0:
                scor = 100 - shift_number
            elif scor - shift_number > 0:
                scor = scor - shift_number
            elif scor - shift_number < 0:
                password += 1
                scor = 100 + (scor - shift_number)
            elif scor - shift_number == 0:
                scor = 0
                password += 1
        else:
            if scor + shift_number <= 99:
                scor+=shift_number
            elif scor + shift_number > 99:
                scor = (scor+shift_number)%100
                password += 1
        file_out.write(f"{shift_direction}{shift_number2},{scor},{password}\n")
        line = file.readline()

        
    print(password)

if __name__ == "__main__":
    solve()


