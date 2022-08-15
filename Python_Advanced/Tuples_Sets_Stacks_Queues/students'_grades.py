students = int(input())
data_dict = {}

for _ in range(students):
    name, grade = input().split()
    if name not in data_dict:
        data_dict[name] = []
    data_dict[name].append(f"{float(grade):.2f}")
avg = 0
average = 0
for student, grade in data_dict.items():
    grades_formatted = " ".join(grade)
    avg = [float(gr) for gr in grade]
    for i in avg:
        average += i
    average /= len(grade)
    print(f"{student} -> {grades_formatted} (avg: {average:.2f})")
    average = 0
