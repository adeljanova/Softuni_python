price_for_1kg_vegetables = float(input())
price_for_1kg_fruits = float(input())
total_kgs_of_vegetables = int(input())
total_kgs_of_fruits = int(input())
total_sum = (price_for_1kg_fruits * total_kgs_of_fruits + price_for_1kg_vegetables * total_kgs_of_vegetables) / 1.94
print(f"{total_sum:.2f}")
