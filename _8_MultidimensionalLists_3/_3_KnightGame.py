def read_board():
    rows = int(input())
    board = []
    for _ in range(rows):
        board.append(list(input()))

    return board


def count_possible_attacks(row, col, board, stats):
    knight_moves = [(-2, +1), (-2, -1),
                    (+2, +1), (+2, -1),
                    (-1, +2), (-1, -2),
                    (+1, +2), (+1, -2)]
    attack_cnt = 0
    attacked_elements = []

    for move in knight_moves:
        new_row = row + move[0]
        new_col = col + move[1]

        if 0 <= new_row < len(board) and 0 <= new_col < len(board[new_row]) and board[new_row][new_col] == "K":
            attacked_elements.append((new_row, new_col))
            attack_cnt += 1
    stats[(row, col)] = attacked_elements
    return attacked_elements


def process_data(board):
    stats = {}

    for i in range(len(board)):
        for j, el in enumerate(board[i]):
            if el == "K":
                count_possible_attacks(i, j, board, stats)

    return sorted(stats.items(), key=lambda item: len(item[1]), reverse=True), stats


# FIX THIS METHOD
def remove_element_until_valid(sorted_stats, board, stats):
    removed_knights = 0
    for _ in sorted_stats:
        knight_pos, elements = sorted_stats[0]
        if len(elements) > 0:
            board[knight_pos[0]][knight_pos[1]] = "0"
            removed_knights += 1
            for attacked_knight in stats[knight_pos]:
                stats[attacked_knight].remove(knight_pos)
            del stats[knight_pos]
            sorted_stats = sorted(stats.items(), key=lambda item: len(item[1]), reverse=True)
    return removed_knights


def start():
    board = read_board()
    sorted_stats, stats = process_data(board)
    removed_knights = remove_element_until_valid(sorted_stats, board, stats)

    for row in range(len(board)):
        print(''.join(board[row]))

    print(removed_knights)


start()
