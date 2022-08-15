start = int(input())
finish = int(input())
magic_number = int(input())
counter = 0
counted = False
for start_num in range(start, finish + 1):
    for finish_num in range(start, finish + 1):
        counter += 1
        if start_num + finish_num == magic_number:

            counted = True
            print(f"Combination N:{counter} ({start_num} + {finish_num} = {magic_number})")
            break
    if counted:
        break
if not counted:
    print(f"{counter} combinations - neither equals {magic_number}")