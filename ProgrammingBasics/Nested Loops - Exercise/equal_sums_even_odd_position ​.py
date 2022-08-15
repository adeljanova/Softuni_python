first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    odd_num_sum = 0
    even_num_sum = 0
    number_str = str(number)
    for index, digit in enumerate(number_str):
        if index % 2 == 0:
            odd_num_sum += int(digit)
        else:
            even_num_sum += int(digit)

    if odd_num_sum == even_num_sum:
        print(number, end=" ")