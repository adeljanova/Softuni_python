first_line = input().split()
second_line = input().split()
third_line = input().split()

first_line_as_digit = []
second_line_as_digit = []
third_line_as_digit = []

for index in range(len(first_line)):
    first_line_as_digit.append(int(first_line[index]))
for index in range(len(second_line)):
    second_line_as_digit.append(int(second_line[index]))
for index in range(len(third_line)):
    third_line_as_digit.append(int(third_line[index]))


for player in range(len(first_line_as_digit)):
    print(first_line_as_digit[player])
    # if first_line_as_digit[player] == 1:
