start = int(input())
finish = int(input())
magic_number = int(input())
counter = 0
sum = 0
flag = False
for first_num in range(start, finish + 1):
    for second_num in range(start, finish + 1):
        sum = first_num + second_num
        counter += 1
        if sum == magic_number:
            print(f"Combination N:{counter} ({first_num} + {second_num} = {magic_number})")
            flag = True
            break
    if flag:
        break
if sum != magic_number:
    print(f"{counter} combinations - neither equals {magic_number}")