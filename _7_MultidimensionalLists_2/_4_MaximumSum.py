def read_matrix():
    dim = list(map(int, input().split(" ")))
    matrix = []
    for i in range(dim[0]):
        line = input().split(" ")
        matrix.append([int(el) for el in line[:dim[1]]])

    return matrix


def find_curr_sum(biggest_sum, matrix, i, j):
    curr_sum = 0
    for x in range(i, i + 3):
        for y in range(j, j + 3):
            curr_sum += matrix[x][y]

    if curr_sum > biggest_sum[0]:
        biggest_sum[0] = curr_sum
        biggest_sum[1] = i
        biggest_sum[2] = j
    return biggest_sum


def find_biggest_sum(matrix):
    biggest_sum = [float("-inf"), -1, -1]
    print(len(matrix))
    for i in range(len(matrix) - 2):
        for j in range(len(matrix[i]) - 2):
            biggest_sum = find_curr_sum(biggest_sum, matrix, i, j)

    return biggest_sum


def print_biggest_sum(biggest_sum, matrix):
    print(f"Sum = {biggest_sum[0]}")
    result = ""

    start_row = biggest_sum[1]
    start_col = biggest_sum[2]

    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            result += str(matrix[i][j]) + " "
        result += "\n"

    print(result)


def start():
    matrix = read_matrix()
    biggest_sum = find_biggest_sum(matrix)
    print_biggest_sum(biggest_sum, matrix)


start()
