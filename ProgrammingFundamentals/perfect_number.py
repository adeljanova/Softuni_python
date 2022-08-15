def perfect_number(number):
    sum = 0
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            sum += i
    if sum == number:
        return "We have a perfect number!"
    return "It's not so perfect."


declared_number = int(input())
print(perfect_number(declared_number))
