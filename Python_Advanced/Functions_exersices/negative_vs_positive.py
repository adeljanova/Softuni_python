def stronger_sum(*args):
    positive_sum = 0
    negative_sum = 0
    for el in args:
        if el < 0:
            negative_sum += el
        else:
            positive_sum += el

    return negative_sum, positive_sum


nums = [int(x) for x in input().split()]

negative_sum, positive_sum = stronger_sum(*nums)
print(negative_sum)
print(positive_sum)

if abs(negative_sum) > positive_sum:
    print("The negatives are stronger than the positives")
else:
    print("The positives are stronger than the negatives")
