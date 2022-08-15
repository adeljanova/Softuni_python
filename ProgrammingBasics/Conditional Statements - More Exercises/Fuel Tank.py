fuel = input()
litres_fuel = float(input())
if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if litres_fuel >= 25:
        print(f"You have enough {fuel.lower()}.")
    elif litres_fuel < 25:
        print(f"Fill your tank with {fuel.lower()}!")
else:
    print(f"Invalid fuel!")