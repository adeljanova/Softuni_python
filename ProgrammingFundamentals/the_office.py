happiness_count = list(map(int, input().split()))
factor = int(input())

average = 0
happy_count = 0
lenght = len(happiness_count)
for i in range(lenght):
    average += happiness_count[i]
average /= lenght

for i in range(lenght):
    if happiness_count[i] >= average:
        happy_count += 1

if happy_count >= average:
    print(f"Score: {happy_count}/{lenght}. Employees are happy!")
else:
    print(f"Score: {happy_count}/{lenght}. Employees are not happy!")