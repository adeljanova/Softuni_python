def tribonacci_sequence(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    else:
        return (tribonacci_sequence(number - 1) +
                tribonacci_sequence(number - 2) +
                tribonacci_sequence(number - 3))


def printTrib(number):
    for i in range(1, number + 1):
        print(tribonacci_sequence(i), end=" ")


declared_number = int(input())
tribonacci_sequence(declared_number)
printTrib(declared_number)