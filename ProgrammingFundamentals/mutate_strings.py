text1 = input()
text2 = input()
string = text1
flag = False
for i in range(len(text1)):
    left_part = text2[:i + 1]
    right_part = text1[i + 1:]
    current_string = left_part + right_part
    if current_string == string:
        continue
    print(current_string)
    string = current_string