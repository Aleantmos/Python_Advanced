def read_matrix():
    dim = list(map(int, input().split(" ")))
    rows = dim[0]
    matrix = []

    for row in range(rows):
        matrix.append(list(map(int, input().split(" "))))

    return matrix


def check_indices_range(indices, row_length, col_length):
    for i, index in enumerate(indices):
        if i % 2 == 0:
            if 0 <= index <= row_length:
                return True
            return False
        else:
            if 0 <= index <= col_length:
                return True
            return False


def process_command(matrix, indices):
    temp = matrix[indices[0]][indices[1]]
    matrix[indices[0]][indices[1]] = matrix[indices[2]][indices[3]]
    matrix[indices[2]][indices[3]] = temp
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join([str(item) for item in row]))


def process_data(matrix):
    tokens = input().split(" ")

    while len(tokens) != 0 and tokens[0] != "END":
        command = tokens[0]
        indices = list(map(int, tokens[1:]))  # Adjust slice as necessary based on expected number of indices
        if command == "swap" and check_indices_range(indices, len(matrix) - 1, len(matrix[0]) - 1):
            matrix = process_command(matrix, indices)
            print_matrix(matrix)

        else:
            print("Invalid input!")
        tokens = input().split(" ")


def start():
    matrix = read_matrix()
    process_data(matrix)


start()
