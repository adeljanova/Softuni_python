num_of_cars = int(input())
parking_lot = set()
for _ in range(num_of_cars):
    command, car_number = input().split(", ")
    if command == "IN":
        parking_lot.add(car_number)
    elif command == "OUT":
        parking_lot.remove(car_number)
if len(parking_lot) > 0:
    [print(car_num) for car_num in parking_lot]
else:
    print("Parking Lot is Empty")





