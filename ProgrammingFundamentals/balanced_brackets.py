num_of_lines = int(input())
string = ""
for i in range(1, num_of_lines + 1):
    random_string = input()
    string += random_string
for j in range(1, num_of_lines + 1):
    if string[j] == ")" and string[j + 1] == "(":
        print("BALANCED")
print("UNBALANCED")

