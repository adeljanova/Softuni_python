data = input()

courses = {}

registered_students = 0
while data != "end":
    course_name, student_name = data.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
        courses[course_name].append(student_name)
    else:
        courses[course_name].append(student_name)
    data = input()

for key in courses.keys():
    for value in courses[key]:
        registered_students += 1
    print(f"{key}: {registered_students}")
    for value in courses[key]:
        print(f"-- {value}")
    registered_students = 0

# print(courses.keys())
# print(courses.values())


