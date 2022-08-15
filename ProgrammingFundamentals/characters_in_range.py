char_one = input()
char_two = input()

new_list = []
def chars_in_between(char1, char2):
    for item in range(ord(char1) + 1, ord(char2)):
        new_list.append(chr(item))
    return new_list

print(*chars_in_between(char_one, char_two))