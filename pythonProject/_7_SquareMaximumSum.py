def read_matrix():
    dim = list(map(int, input().split(", ")))
    rows = dim[0]
    matrix = []
    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)

    return matrix


def get_sum(matrix, top_sum, top_index, r, c):
    curr_sum = matrix[r][c] + matrix[r + 1][c] + matrix[r][c + 1] + matrix[r + 1][c + 1]

    if curr_sum > top_sum:
        top_sum = curr_sum
        top_index = r, c

    return top_sum, top_index


def find_biggest_sum(matrix):
    top_sum = 0
    top_index = [-1, -1]

    for r in range(len(matrix) - 1):
        for c in range(len(matrix[r]) - 1):
            top_sum, top_index = get_sum(matrix, top_sum, top_index, r, c)

    return top_sum, top_index


def print_top_matrix(top_index, matrix):
    r = top_index[0]
    c = top_index[1]
    result = f"{matrix[r][c]} {matrix[r][c + 1]}\n{matrix[r + 1][c]} {matrix[r + 1][c + 1]}"
    print(result)


def print_result(top_sum, top_index, matrix):
    print_top_matrix(top_index, matrix)
    print(top_sum)


def start():
    matrix = read_matrix()
    top_sum, top_index = find_biggest_sum(matrix)
    
    print_result(top_sum, top_index, matrix)


start()
