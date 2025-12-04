def take_input():
    matrix = []
    file = open("input.txt", "r")
    row = file.readline()
    while row:
        row = list(row)
        if row[len(row)-1] == '\n':
            row = row[:len(row)-1]
        matrix.append(row)
        row = file.readline()
    print(matrix)
    return matrix

def write_output(matrix):
    file = open("output.txt", "w")
    file.write(matrix)

def count_neighbors(i, n, j, m, matrix):
    start_i = -1
    end_i = -1
    start_j = -1
    end_i = -1
    if i == 0:
        start_i = 0
        end_i = 1
    elif i == n-1:
        start_i = n-2
        end_i = n-1
    else:
        start_i = i-1
        end_i = i+1
    if j == 0:
        start_j = 0
        end_j = 1
    elif j == m-1:
        start_j = m-2
        end_j = m-1
    else:
        start_j = j-1
        end_j = j + 1

    neighbor_count = 0
    #print()
    #print(f"i={i}, j={j}, start_i={start_i}, start_j={start_j}, end_i={end_i}, end_j={end_j}")
    for n_i in range(start_i, end_i + 1):
        for n_j in range(start_j, end_j +1):
            #print(n_i, n_j,matrix[n_i][n_j])
            if matrix[n_i][n_j] == '@':
                #print("OK")
                neighbor_count+=1
    #print(i, j, neighbor_count)

    return neighbor_count-1
            



def solve(matrix):
    matrix_new = ""
    n = len(matrix)
    total = 0
    for i in range(0,n):
        m = len(matrix[i])
        for j in range(0,m):
            if matrix[i][j] == '@':
                neighbor_count = count_neighbors(i,n,j,m,matrix)
                if neighbor_count < 4:
                    matrix_new = "".join([matrix_new, "x"])
                    total += 1
                else:
                    matrix_new = "".join([matrix_new,matrix[i][j]])
            else:
                matrix_new = "".join([matrix_new,matrix[i][j]])
        matrix_new="".join([matrix_new,"\n"])

    
    print(total)
    return total, matrix_new

def matrix_string_to_actual_matrix(matrix_string): #kill me
    matrix = matrix_string.split("\n")
    matrix_new = []
    for a in matrix:
        a = list(a)
        matrix_new.append(a)
    print(matrix_new)
    return matrix_new[:len(matrix_new) - 1]

def solve2():
    total, matrix_new = solve(take_input())
    sum = 0
    while total != 0:
        print(total)
        sum += total
        matrix_new = matrix_string_to_actual_matrix(matrix_new)
        total,matrix_new = solve(matrix_new)
    print(sum)


solve2()