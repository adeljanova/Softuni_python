word_one, word_two = input().split()

total_sum = 0

char_codes_one = [ord(ch) for ch in word_one]
char_codes_two = [ord(ch) for ch in word_two]

if len(word_one) > len(word_two):
    for i in range(len(word_two)):
        total_sum += char_codes_one[i] * char_codes_two[i]
    for j in range(len(word_two), len(word_one)):
        total_sum += char_codes_one[j]
elif len(word_one) < len(word_two):
    for i in range(len(word_one)):
        total_sum += char_codes_one[i] * char_codes_two[i]
    for j in range(len(word_one), len(word_two)):
        total_sum += char_codes_two[j]
else:
    for i in range(len(word_one)):
        total_sum += char_codes_one[i] * char_codes_two[i]
print(total_sum)


