obtained_cars = int(input())

cars_dict = {}
for i in range(obtained_cars):
    car, mileage, fuel = input().split("|")
    cars_dict[car] = [int(mileage), int(fuel)]

input_data = input()

while input_data != "Stop":
    split_data = input_data.split(" : ")
    command, car = split_data[0], split_data[1]
    if command == "Drive":
        distance, fuel = int(split_data[2]), int(split_data[3])
        if cars_dict[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars_dict[car][0] += distance
            cars_dict[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars_dict[car][0] >= 100000:
                print(f"Time to sell the {car}!")
                del cars_dict[car]
    elif command == "Refuel":
        fuel = int(split_data[2])
        cars_dict[car][1] += fuel
        if cars_dict[car][1] >= 75:
            print(f"{car} refueled with {abs(cars_dict[car][1] - 75 - fuel)} liters")
            cars_dict[car][1] = 75
        else:
            print(f"{car} refueled with {fuel} liters")
    elif command == "Revert":
        kilometres = int(split_data[2])
        cars_dict[car][0] -= kilometres
        if cars_dict[car][0] < 10000:
            cars_dict[car][0] = 10000
        else:
            print(f"{car} mileage decreased by {kilometres} kilometers")
    input_data = input()

for key, value in cars_dict.items():
    print(f"{key} -> Mileage: {cars_dict[key][0]} kms, Fuel in the tank: {cars_dict[key][1]} lt.")
