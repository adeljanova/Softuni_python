def rounding(numbers):
    for item in range(len(list_of_numbers)):
        new_list.append(round(float(list_of_numbers[item])))
    return new_list

list_of_numbers = input().split()
new_list = []
print(rounding(list_of_numbers))
