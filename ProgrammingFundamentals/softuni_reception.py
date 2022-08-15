first_employee_per_hour = int(input())
second_employee_per_hour = int(input())
third_employee_per_hour = int(input())
student_count = int(input())
counter = 0
total_per_hour = first_employee_per_hour + second_employee_per_hour + third_employee_per_hour
while student_count > 0:
    counter += 1
    if counter % 4 == 0:
        continue
    else:
        student_count -= total_per_hour
print(f"Time needed: {counter}h.")