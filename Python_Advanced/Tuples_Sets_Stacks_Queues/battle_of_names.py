n = int(input())

odd_set = set()
even_set = set()
sum = 0

for i in range(1, n + 1):
    current_name = input()
    for char in current_name:
        sum += ord(char)
    sum //= i

    if sum % 2 == 0:
        even_set.add(sum)
    else:
        odd_set.add(sum)

    sum = 0

even_sum = 0
odd_sum = 0

for num in even_set:
    even_sum += num
for num in odd_set:
    odd_sum += num

if even_sum == odd_sum:
    even_set.union(odd_set)
    even_set = map(str, even_set)
    print(', '.join(even_set))
elif even_sum > odd_sum:
    even_set.symmetric_difference_update(odd_set)
    even_set = map(str, even_set)
    print(', '.join(even_set))
else:
    # odd_set.difference_update(even_set)
    odd_set = map(str, odd_set)
    print(", ".join(odd_set))