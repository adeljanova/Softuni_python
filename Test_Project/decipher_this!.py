decripted_message = input()
split_data = decripted_message.split()

temp_dig = ''
temp_ch = ''
temp = ''
new_line = ''
new_word = ''
for word in split_data:
    for ch in word:
        if ch.isdigit():
            temp_dig += ch
        else:
            temp_ch += ch
    temp = int(temp_dig)
    new_word += chr(temp)
    char_list = [i for i in temp_ch]
    char_list[0], char_list[-1] = char_list[-1], char_list[0]
    for i in char_list:
        new_word += i
    new_line += new_word
    new_line += " "
    temp_dig = ''
    temp_ch = ''
    temp = ''
    char_list = []
    new_word = ''
print(new_line)


