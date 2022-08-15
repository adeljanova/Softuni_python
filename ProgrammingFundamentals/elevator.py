import math

num_people = int(input())
capacity = int(input())
courses = num_people // capacity
people = math.ceil(num_people / capacity)
print(people)

