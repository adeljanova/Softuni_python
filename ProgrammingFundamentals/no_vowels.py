command = input()
vowels = ['a', 'u', 'e', 'i', 'o', 'A', 'U', 'E', 'I', 'O']

new_list = ''.join([i for i in command if i not in vowels])
print(new_list)


