def read_matrix():
    rows = int(input())
    matrix = []

    for _ in range(rows):
        row = list(map(int, input().split(", ")))
        matrix.append(row)
    return matrix


def process_matrix(matrix):
    for row in matrix:
        for num in row:
            if num % 2 == 1:
                row.remove(num)

    return matrix


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))

    print(matrix)


def main():
    matrix = read_matrix()

    processed = process_matrix(matrix)

    print_matrix(processed)


main()
