text = input()

output_set = set()

for letter in text:
    output_set.add((letter, text.count(letter)))

for pair in sorted(output_set):
    print(f"{pair[0]}: {pair[1]} time/s")