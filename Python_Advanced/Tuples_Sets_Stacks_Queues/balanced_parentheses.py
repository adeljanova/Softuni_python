from collections import deque

sequence_of_parentheses = input()
split_sequence = [i for i in sequence_of_parentheses]
queue = deque(split_sequence)
left_part = []
right_part = []

length = len(split_sequence)
for i in range(length):
    if i > ((length/2) - 1):
        right_part.append(queue.popleft())
    else:
        left_part.append(queue.popleft())

right_part = deque(right_part)
left_part = deque(left_part)
is_valid = False
while left_part and right_part:
    temp_left = left_part.popleft()
    temp_right = right_part.pop()
    temp_brackets = temp_left + temp_right
    if temp_brackets == "{}" or temp_brackets == "()" or temp_brackets == "[]":
        is_valid = True
    else:
        is_valid = False
        break

if is_valid:
    print("YES")
else:
    print("NO")
