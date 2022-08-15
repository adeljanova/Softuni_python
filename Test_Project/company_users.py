command = input()

company_tracker = {}

while command != "End":
    company_name, employee_id = command.split(" -> ")
    if company_name not in company_tracker:
        company_tracker[company_name] = []
        company_tracker[company_name].append(employee_id)
    else:
        if employee_id not in company_tracker[company_name]:
            company_tracker[company_name].append(employee_id)
    command = input()

for key in company_tracker.keys():
    print(f"{key}")
    for value in company_tracker[key]:
        print(f"-- {value}")
