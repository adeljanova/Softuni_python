season = input()
group_type = input()
students = int(input())
nights = int(input())
nights_price = 0
sport = ""
if group_type in "girls boys":
    if season == "Winter":
        nights_price = 9.60
    elif season == "Spring":
        nights_price = 7.20
    elif season == "Summer":
        nights_price = 15
elif group_type == "mixed":
    if season == "Winter":
        nights_price = 10
    elif season == "Spring":
        nights_price = 9.50
    elif season == "Summer":
        nights_price = 20
total_price = nights * nights_price * students
if students >= 50:
    total_price -= total_price * 0.50
elif 20 <= students < 50:
    total_price -= total_price * 0.15
elif 10 <= students < 20:
    total_price -= total_price * 0.05
if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    elif season == "Summer":
        sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    elif season == "Summer":
        sport = "Football"
elif group_type == "mixed":
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    elif season == "Summer":
        sport = "Swimming"
print(f"{sport} {total_price:.2f} lv.")
