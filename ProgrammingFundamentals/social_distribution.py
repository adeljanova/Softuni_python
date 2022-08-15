import sys

population = list(map(int, input().split(", ")))

minimum_wealth = int(input())

max_num = -sys.maxsize

number_counter = 0
for number in range(len(population)):
    number_counter += 1
    if population[number] > max_num:
        max_num = population[number]
population.remove(max_num)

for people in range(len(population)):
    if population[people] < minimum_wealth:
        difference = minimum_wealth - population[people]
        population[people] += difference
        max_num -= difference
    if max_num < minimum_wealth:
        population.insert(number_counter, max_num)
        break

if max_num < minimum_wealth:
    print("No equal distribution possible")
else:
    population.insert(number_counter, max_num)
    print(population)