first_digit_first_number = int(input())
second_digit_first_number = int(input())
first_digit_second_number = int(input())
second_digit_second_number = int(input())
number_one = 0
number_two = 0
counter = 0
limit = False
for first in range(first_digit_first_number, 9):
    for second in range(9, second_digit_first_number - 1, -1):
        number_one = str(first) + str(second)
        number_one_as_int = int(number_one)
        for third in range(first_digit_second_number, 9):
            for fourth in range(9, second_digit_second_number - 1, -1):
                number_two = str(third) + str(fourth)
                number_two_as_int = int(number_two)
                if first % 2 == 0 and third % 2 == 0 and second % 2 != 0 and fourth % 2 != 0:
                    if number_one_as_int == number_two_as_int:
                        print("Cannot change the same player.")
                    else:
                        counter += 1
                        print(f"{first}{second} - {third}{fourth}")
                    if counter == 6:
                        limit = True
                        break
            if limit:
                break
        if limit:
            break
    if limit:
        break







