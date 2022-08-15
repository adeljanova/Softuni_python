def can_black_pick_white(b_row, b_col, w_row, w_col):
    positions_b = [
        (b_row - 1, b_col - 1),
        (b_row - 1, b_col + 1),
        (b_row + 1, b_col - 1),
        (b_row + 1, b_col + 1),
    ]

    if (w_row, w_col) in positions_b:
        return True
    return False


def can_white_pick_black(w_row, w_col, b_row, b_col):
    positions_w = [
        (w_row - 1, w_col - 1),
        (w_row - 1, w_col + 1),
        (w_row + 1, w_col - 1),
        (w_row + 1, w_col + 1),
    ]

    if (b_row, b_col) in positions_w:
        return True
    return False


def white_position(w_row, w_col, b_row, b_col):
    w_row = b_row
    w_col = b_col
    return w_row, w_col


def black_position(b_row, b_col, w_row, w_col):
    b_row = w_row
    b_col = w_col
    return b_row, b_col


white_row = 0
white_col = 0
black_row = 0
black_col = 0

matrix = []
for row in range(8):
    line = input().split()
    matrix.append(line)
    for col in range(len(line)):
        if line[col] == "b":
            black_row = row
            black_col = col
        elif line[col] == "w":
            white_row = row
            white_col = col

is_black_queen = False
is_white_queen = False
is_black_winner = False
is_white_winner = False
counter = 1
while True:

    if counter % 2 == 0:
        if can_black_pick_white(black_row, black_col, white_row, white_col):
            black_row, black_col = black_position(black_row, black_col, white_row, white_col)
            is_black_winner = True
            break
        black_row += 1
    else:
        if can_white_pick_black(white_row, white_col, black_row, black_col):
            white_row, white_col = white_position(white_row, white_col, black_row, black_col)
            is_white_winner = True
            break
        white_row -= 1

    if white_row == 0:
        is_white_queen = True
        break
    elif black_row == 7:
        is_black_queen = True
        break

    counter += 1

letters = {
    0: "a",
    1: "b",
    2: "c",
    3: "d",
    4: "e",
    5: "f",
    6: "g",
    7: "h",
}
end_row = 0
end_col = 0
found_pos = False
for r in range(8):
    for c in range(8):
        if (r == white_row and c == white_col) or (r == black_row and c == black_col):
            end_row = 8 - r
            end_col = letters[c]
            found_pos = True
    if found_pos:
        break
if is_black_queen:
    print(f"Game over! Black pawn is promoted to a queen at {end_col + str(end_row)}.")
elif is_white_queen:
    print(f"Game over! White pawn is promoted to a queen at {end_col + str(end_row)}.")

if is_black_winner:
    print(f"Game over! Black win, capture on {end_col + str(end_row)}.")
elif is_white_winner:
    print(f"Game over! White win, capture on {end_col + str(end_row)}.")
