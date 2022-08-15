secret_message = input().split()

deciphered_word = []
deciphered_list = []
for message in secret_message:
    secret_word = message.split(", ")

    # for item in secret_word:


#     secret_word = list(map(int, message))
#     for letter in secret_word:
#         if secret_word[letter] == 1:
#             secret_word[letter], secret_word[len(secret_word)] =\
#                 secret_word[len(secret_word)], secret_word[letter]
#             deciphered_word.append(chr(letter))
#         else:
#             deciphered_word.append(chr(letter))
#     deciphered_list.append(deciphered_word)
# print(deciphered_list)


