name = input()
average_grade = 0
school_class = 0
is_excluded = True
class_failed = 0
while is_excluded:
    grade = float(input())
    if grade >= 4:
        average_grade += grade
        school_class += 1
        if school_class == 12:
            average_grade /= 12
            print(f"{name} graduated. Average grade: {average_grade:.2f}")
            break
    else:
        class_failed += 1
        if class_failed == 2:
            school_class += 1
            is_excluded = False
            print(f"{name} has been excluded at {school_class} grade")
            continue



