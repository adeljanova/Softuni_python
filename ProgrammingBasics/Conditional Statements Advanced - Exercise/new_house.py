type_flowers = input()
number_flowers = int(input())
budget = int(input())
total_price = 0
if type_flowers == "Roses":
    total_price = number_flowers * 5
    if number_flowers > 80:
        total_price -= total_price * 0.10
elif type_flowers == "Dahlias":
    total_price = number_flowers * 3.80
    if number_flowers > 90:
        total_price -= total_price * 0.15
elif type_flowers == "Tulips":
    total_price = number_flowers * 2.80
    if number_flowers > 80:
        total_price -= total_price * 0.15
elif type_flowers == "Narcissus":
    total_price = number_flowers * 3
    if number_flowers < 120:
        total_price += total_price * 0.15
elif type_flowers == "Gladiolus":
    total_price = number_flowers * 2.50
    if number_flowers < 80:
        total_price += total_price * 0.20
sum_left = abs(budget - total_price)
if total_price <= budget:
    print(f"Hey, you have a great garden with {number_flowers} {type_flowers} and {sum_left:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum_left:.2f} leva more.")