def words_sorting(*args):
    sum_dict = {}
    temp_sum = 0
    total_sum = 0
    result = []
    for word in args:
        for letter in word:
            temp_sum += ord(letter)
        sum_dict[word] = temp_sum
        total_sum += temp_sum
        temp_sum = 0

    if total_sum % 2 == 0:
        result = [f"{key} - {value}" for key, value in
                  sorted(sum_dict.items(), key=lambda x: x[0])]
    else:
        result = [f"{key} - {value}" for key, value in
                  sorted(sum_dict.items(), key=lambda x: -x[1])]
    return "\n".join(result)

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))
print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
print(
    words_sorting(
        'cacophony',
        'accolade'
  ))
