large_piece_width = int(input())
large_piece_height = int(input())
small_piece_width = int(input())
small_piece_height = int(input())

max_num_of_plates = 0
if large_piece_width // small_piece_width == 1:
    if large_piece_width == small_piece_width:
        max_num_of_plates = large_piece_height // small_piece_height
    elif large_piece_width == small_piece_height:
        max_num_of_plates = large_piece_height // small_piece_width
    elif large_piece_height == small_piece_width:
        max_num_of_plates = large_piece_width // small_piece_height
    elif large_piece_height == small_piece_height:
        max_num_of_plates = large_piece_width // small_piece_width
elif large_piece_width // small_piece_width > 1:
    if large_piece_height >= small_piece_height:
        max_num_of_plates = (large_piece_height // small_piece_height) * (large_piece_width // small_piece_width)
    else:
        if large_piece_width > small_piece_width:
            max_num_of_plates = large_piece_height // small_piece_width
        else:
            max_num_of_plates = 0



print(max_num_of_plates)