expression = list(input())

stack_holder = []

for index,el in enumerate(expression):
    if el == "(":
        stack_holder.append(index)
    elif el == ")":
        print(''.join(expression[stack_holder[-1]:index+1]))
        stack_holder.pop()