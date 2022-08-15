jury = int(input())
presentation_name = input()
average_grade = 0
counter = 0
total_average = 0
total_grades = 0
while presentation_name != "Finish":
    for gr in range(1, jury + 1):
        grade = float(input())
        total_grades += 1
        total_average += grade
        average_grade += grade
        counter += 1
        if counter == jury:
            print(f"{presentation_name} - {(average_grade / counter):.2f}.")
            break
    average_grade = 0
    counter = 0
    presentation_name = input()
if presentation_name == "Finish":
    print(f"Student's final assessment is {(total_average / total_grades):.2f}.")








