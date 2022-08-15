juniors = int(input())
seniors = int(input())
type_of_route = input()
total_tax_juniors = 0
total_tax_seniors = 0
total_competitors = juniors + seniors
money_after_expences = 0

if type_of_route == "trail":
    total_tax_juniors = juniors * 5.50
elif type_of_route == "cross-country":
    total_tax_juniors = juniors * 8
elif type_of_route == "downhill":
    total_tax_juniors = juniors * 12.25
elif type_of_route == "road":
    total_tax_juniors = juniors * 20
if type_of_route == "trail":
    total_tax_seniors = seniors * 7
elif type_of_route == "cross-country":
    total_tax_seniors = seniors * 9.50
elif type_of_route == "downhill":
    total_tax_seniors = seniors * 13.75
elif type_of_route == "road":
    total_tax_seniors = seniors * 21.50
total_tax = total_tax_juniors + total_tax_seniors
if type_of_route == "cross-country" and total_competitors >= 50:
    total_tax -= total_tax * 0.25
money_after_expences = total_tax * 0.95
print(f"{money_after_expences:.2f}" )


