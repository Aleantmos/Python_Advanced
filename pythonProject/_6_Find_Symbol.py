def read_matrix():
    dim = int(input())
    matrix = []
    for _ in range(dim):
        row = list(input())
        matrix.append(row)

    find_element = input()

    return matrix, find_element


def find_element_in_matrix(matrix, element):
    for i, row in enumerate(matrix):
        for j, el in enumerate(row):
            if el == element:
                return i, j


def main():
    matrix, element = read_matrix()
    row_index, col_index = find_element_in_matrix(matrix, element)

    print(f"({row_index}, {col_index})")


main()
