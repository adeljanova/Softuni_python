clothes = input().split()
capacity = int(input())

number_of_racks = 1

current_capacity = capacity
while clothes:
    current_piece_of_clothing = int(clothes[-1])
    if current_piece_of_clothing <= current_capacity:
        current_capacity -= current_piece_of_clothing
        clothes.pop()
    else:
        current_capacity = capacity
        number_of_racks += 1
print(number_of_racks)