def multiplication(num1, num2, num3):
    if num1 < 0 or num2 < 0 or num3 < 0:
        if num1 == 0 or num2 == 0 or num3 == 0:
            print("zero")
        else:
            print("negative")
    elif num1 > 0 and num2 > 0 and num3 > 0:
        print("positive")
    else:
        print("zero")


number_one = int(input())
number_two = int(input())
number_three = int(input())

multiplication(number_one, number_two, number_three)