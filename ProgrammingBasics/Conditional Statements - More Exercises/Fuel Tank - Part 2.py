fuel = input()
litres_fuel = float(input())
club_card = input()
price_gasoline = 2.22
price_diesel = 2.33
price_gas = 0.93
if club_card == "Yes":
    if fuel == "Gasoline":
        total_fuel = litres_fuel * (price_gasoline - 0.18)
    elif fuel == "Diesel":
        total_fuel = litres_fuel * (price_diesel - 0.12)
    elif fuel == "Gas":
        total_fuel = litres_fuel * (price_gas - 0.08)
elif club_card == "No":
    if fuel == "Gasoline":
        total_fuel = litres_fuel * price_gasoline
    elif fuel == "Diesel":
        total_fuel = litres_fuel * price_diesel
    elif fuel == "Gas":
        total_fuel = litres_fuel * price_gas
if 20 <= litres_fuel <= 25:
    total_fuel -= total_fuel * 0.08
elif litres_fuel > 25:
    total_fuel -= total_fuel * 0.10
print(f"{total_fuel:.2f} lv.")