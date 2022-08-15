square_feet = float(input())
price_of_square_feet = 7.61
discount = 0.18 * (square_feet * price_of_square_feet)
final_price = (square_feet * price_of_square_feet) - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is: {discount} lv.")