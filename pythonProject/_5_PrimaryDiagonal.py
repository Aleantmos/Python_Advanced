def read_matrix():
    dim = int(input())
    matrix = []
    for _ in range(dim):
        row = list(map(int, input().split(" ")))
        matrix.append(row)

    return matrix


def get_primary_diagonal_sum(matrix):
    diagonal_sum = 0
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if i == j:
                diagonal_sum += el

    return diagonal_sum


def main():
    matrix = read_matrix()

    result = get_primary_diagonal_sum(matrix)

    print(result)


main()
