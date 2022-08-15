data = input()

courses = {}

while ":" in data:
    name, ID, course = data.split(":")
    if course not in courses:
        courses[course] = {}
    courses[course][ID] = name
    data = input()

line = " ".join(data.split("_"))
for key, value in courses.items():
    if key == line:
        for ID, name in value.items():
            print(f"{name} - {ID}")


