string_of_numbers = list(map(int, input().split(", ")))

new_list = [i for i in range(len(string_of_numbers)) if string_of_numbers[i] % 2 == 0]
print(new_list)