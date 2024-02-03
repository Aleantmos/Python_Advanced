def read_matrix():
    dim = list(map(int, input().split(" ")))
    matrix = []
    for i in range(dim[0]):
        line = input().split(" ")
        matrix.append(line[:dim[1]])

    return matrix


def identical_elements(el, matrix, i, j):
    return el == matrix[i + 1][j] == matrix[i][j + 1] == matrix[i + 1][j + 1]


def find_identical(matrix):
    count = 0

    for i, row in enumerate(matrix[:-1]):
        for j, el in enumerate(row[:-1]):
            if identical_elements(el, matrix, i, j):
                count += 1

    return count


def main():
    matrix = read_matrix()

    result = find_identical(matrix)

    print(result)


main()
