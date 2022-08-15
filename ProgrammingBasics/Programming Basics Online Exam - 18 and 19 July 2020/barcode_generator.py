first_number = int(input())
second_number = int(input())
digit_one = 0
digit_two = 0
digit_three = 0
digit_four = 0
is_valid = False
first_number_as_str = str(first_number)
second_number_as_str = str(second_number)
for first in range(int(first_number_as_str[0]), int(second_number_as_str[0]) + 1):
    for second in range(int(first_number_as_str[1]), int(second_number_as_str[1]) + 1):
        for third in range(int(first_number_as_str[2]), int(second_number_as_str[2]) + 1):
            for fourth in range(int(first_number_as_str[3]), int(second_number_as_str[3]) + 1):
                if first % 2 != 0 and second % 2 != 0 and third % 2 != 0 and fourth % 2 != 0:
                    digit_one = first
                    digit_two = second
                    digit_three = third
                    digit_four = fourth
                    print(f"{digit_one}{digit_two}{digit_three}{digit_four}", end=" ")











