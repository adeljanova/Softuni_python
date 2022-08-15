def age_assignment(*args, **kwargs):
    result = {}
    for letter, age in kwargs.items():
        for name in args:
            if letter in name:
                result[name] = age
    result = sorted(result.items(), key=lambda x: x[0])
    output = []

    for item in result:
        output.append(f"{item[0]} is {item[1]} years old.")

    return '\n'.join(output)


print(age_assignment("Peter", "George", G=26, P=19))
print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
