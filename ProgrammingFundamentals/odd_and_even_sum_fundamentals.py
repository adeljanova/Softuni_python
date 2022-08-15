def sum_odd_even(num):
    sum_odd = 0
    sum_even = 0
    while num > 0:
        temp = num % 10
        if temp % 2 == 0:
            sum_even += temp
        else:
            sum_odd += temp
        num //= 10
    return f"Odd sum = {sum_odd}, Even sum = {sum_even}"

number = int(input())
print(sum_odd_even(number))