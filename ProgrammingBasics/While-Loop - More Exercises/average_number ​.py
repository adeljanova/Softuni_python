number = int(input())
average = 0
counter = 0
for num in range(number):
    score = int(input())
    counter += 1
    average += score
print(f"{(average / counter):.2f}")
