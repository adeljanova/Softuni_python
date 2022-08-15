type_projection = input()
rows = int(input())
columns = int(input())
total_count = rows * columns
price = 0
if type_projection == "Premiere":
    price = total_count * 12.00
elif type_projection == "Normal":
    price = total_count * 7.50
elif type_projection == "Discount":
    price = total_count * 5
print(f"{price:.2f} leva")