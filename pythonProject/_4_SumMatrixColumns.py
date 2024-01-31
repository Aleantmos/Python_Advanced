def read_matrix():
    dim = list(map(int, input().split(", ")))
    matrix = []
    for _ in range(dim[0]):
        row = list(map(int, input().split(" ")))
        matrix.append(row)

    return matrix


def sum_columns(matrix):
    column_count = len(matrix[0])
    sums = [0] * column_count

    for row in matrix:
        for j in range(len(row)):
            sums[j] += row[j]

    return sums


def main():
    matrix = read_matrix()
    result = sum_columns(matrix)
    print(result)


main()
