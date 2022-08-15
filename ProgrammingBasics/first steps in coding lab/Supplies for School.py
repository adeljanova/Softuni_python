price_of_package_of_pens = 5.80
price_of_package_of_markers = 7.20
price_of_litre_of_detergent = 1.20
number_of_pens = int(input())
number_of_markers = int(input())
number_of_litre_of_detergent = int(input())
discount_percent = int(input())
total_price_pens = price_of_package_of_pens * number_of_pens
total_price_markers = price_of_package_of_markers * number_of_markers
total_price_detergent = price_of_litre_of_detergent * number_of_litre_of_detergent
total_price = total_price_detergent + total_price_markers + total_price_pens
total_price_with_discount = total_price - (total_price * (discount_percent / 100))
print(total_price_with_discount)
