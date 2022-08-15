students = int(input())
student_f = 0
student_c_d = 0
student_d_b = 0
student_b_a = 0
grade_f = 0
grade_c_d = 0
grade_d_b = 0
grade_b_a = 0
for student in range(students):
    grade = float(input())
    if 2.00 <= grade <= 2.99:
        grade_f += grade
        student_f += 1
    elif 3 <= grade <= 3.99:
        grade_c_d += grade
        student_c_d += 1
    elif 4 <= grade <= 4.99:
        grade_d_b += grade
        student_d_b += 1
    elif 5 <= grade <= 6:
        grade_b_a += grade
        student_b_a += 1
percent_f = (student_f / students) * 100
percent_c_d = (student_c_d / students) * 100
percent_d_b = (student_d_b / students) * 100
percent_b_a = (student_b_a / students) * 100
average = (grade_f + grade_c_d + grade_d_b + grade_b_a) / students
print(f"Top students: {percent_b_a:.2f}%")
print(f"Between 4.00 and 4.99: {percent_d_b:.2f}%")
print(f"Between 3.00 and 3.99: {percent_c_d:.2f}%")
print(f"Fail: {percent_f:.2f}%")
print(f"Average: {average:.2f}")