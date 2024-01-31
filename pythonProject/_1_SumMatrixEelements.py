def read_matrix():
    rows, cols = map(int, input().split(", "))

    matrix = []

    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)

    return matrix


def sum_matrix(matrix):
    total_sum = 0
    for row in matrix:
        total_sum += sum(row)
    return total_sum


def print_result(matrix, result):
    print(f"The sum of all numbers in the matrix is: {result}")

    for row in matrix:
        print(" ".join(map(str, row)))


def main():
    matrix = read_matrix()

    result = sum_matrix(matrix)

    print_result(matrix, result)

main()
