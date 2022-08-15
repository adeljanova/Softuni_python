def fill_the_box(*args):
    total_space = 1
    for el in args[0:3]:
        total_space *= el

    sum_of_nums = 0
    for el in args[3:]:
        if el == "Finish":
            break
        else:
            sum_of_nums += el
    if total_space <= sum_of_nums:
        return f"No more free space! You have {sum_of_nums - total_space} more cubes."
    return f"There is free space in the box. You could put {total_space - sum_of_nums} more cubes."


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))
