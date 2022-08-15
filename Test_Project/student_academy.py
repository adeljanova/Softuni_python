n = int(input())

student_tracker = {}

counter = 0
average = 0
average_sum = 0
for _ in range(n):
    student_name = input()
    grade = float(input())
    if student_name not in student_tracker:
        student_tracker[student_name] = []
        student_tracker[student_name].append(grade)
    else:
        student_tracker[student_name].append(grade)

for key in student_tracker.keys():
    for value in student_tracker[key]:
        counter += 1
        average_sum += value
    average = average_sum / counter
    student_tracker[key] = average
    counter = 0
    average_sum = 0

output = [print(f"{key} -> {value:.2f}") for key, value in student_tracker.items() if value >= 4.50]

