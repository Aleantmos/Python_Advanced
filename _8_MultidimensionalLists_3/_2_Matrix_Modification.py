def read_data():
    rows = int(input())

    matrix = []

    for row in range(rows):
        matrix.append(list(map(int, input().split(" "))))

    return matrix


def do_add_operation(cur_row, cur_col, amount, matrix):
    matrix[cur_row][cur_col] += amount
    return matrix


def convert_data_str_to_int(data):
    cur_row = int(data[1])
    cur_col = int(data[2])
    amount = int(data[3])

    return cur_row, cur_col, amount


def do_subtract_operation(cur_row, cur_col, amount, matrix):
    matrix[cur_row][cur_col] -= amount
    return matrix


def valid_coordinates(cur_row, cur_col, matrix):
    return 0 <= cur_row < len(matrix) and 0 <= cur_col < len(matrix[cur_row])


def perform_command(data, matrix):
    command = data[0]
    cur_row, cur_col, amount = convert_data_str_to_int(data)
    if not valid_coordinates(cur_row, cur_col, matrix):
        print("Invalid index")
    else:
        if command == "Add":
            do_add_operation(cur_row, cur_col, amount, matrix)
        elif command == "Subtract":
            do_subtract_operation(cur_row, cur_col, amount, matrix)
    return matrix


def process_commands(matrix):
    data = input().split(" ")

    while data[0] != "END":
        perform_command(data, matrix)

        data = input().split(" ")

    return matrix


def print_matrix(matrix):
    joined_rows = [" ".join(map(str, row)) for row in matrix]

    result_str = "\n".join(joined_rows)

    print(result_str)


def start():
    matrix = read_data()

    matrix_result = process_commands(matrix)

    print_matrix(matrix_result)


start()
