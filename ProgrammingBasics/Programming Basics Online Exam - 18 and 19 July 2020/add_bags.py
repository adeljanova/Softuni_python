luggage_over_20 = float(input())
kg_luggage = float(input())
days_till_trip = int(input())
num_luggage = int(input())
tax_luggage = 0
price = 0
if kg_luggage < 10:
    tax_luggage = luggage_over_20 * 0.2
    price += tax_luggage
elif 10 <= kg_luggage <= 20:
    tax_luggage = luggage_over_20 * 0.5
    price += tax_luggage
else:
    tax_luggage = luggage_over_20
    price += tax_luggage

if days_till_trip > 30:
    price += price * 0.1
elif 7 <= days_till_trip <= 30:
    price += price * 0.15
else:
    price += price * 0.4
total_price = price * num_luggage
print(f"The total price of bags is: {total_price:.2f} lv.")