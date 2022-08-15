unpleasant_grades = int(input())
problem_name = input()
average_grade = 0
all_problems = 0
poor_grades = 0
last_problem = ""
while problem_name != "Enough":
    grade = int(input())
    if grade <= 4:
        poor_grades += 1
        if poor_grades == unpleasant_grades:
            print(f"You need a break, {unpleasant_grades} poor grades.")
            break
    average_grade += grade
    all_problems += 1
    last_problem = problem_name
    problem_name = input()
average_grade /= all_problems
if problem_name == "Enough":
    print(f"Average score: {average_grade:.2f}")
    print(f"Number of problems: {all_problems}")
    print(f"Last problem: {last_problem}")