def read_data():
    dim = list(map(int, input().split(" ")))
    str_chars = list(input())
    return dim, str_chars


def build_snake(dim, chars):
    rows = int(dim[0])
    rows_count = 0

    cols = int(dim[1])

    curr_str_index = 0
    chars_length = len(chars)
    while rows_count < rows:
        result = ""
        for i in range(cols):
            result += chars[curr_str_index]
            curr_str_index += 1
            if curr_str_index == chars_length:
                curr_str_index = 0

        if rows_count % 2 == 1:
            result = ''.join(reversed(result))
        print(result)

        rows_count += 1


def start():
    dim, str_chars = read_data()
    build_snake(dim, str_chars)


start()
