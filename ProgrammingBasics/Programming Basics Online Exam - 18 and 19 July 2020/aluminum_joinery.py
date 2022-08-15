num_joinery = int(input())
type_joinery = input()
ways_received = input()
price = 0
if num_joinery > 10:
    if type_joinery == "90X130":
        if 30 < num_joinery < 60:
            price = (num_joinery * 110) * 0.95
        elif num_joinery > 60:
            price = (num_joinery * 110) * 0.92
        elif num_joinery < 30:
            price = num_joinery * 110
    elif type_joinery == "100X150":
        if 40 < num_joinery < 80:
            price = (num_joinery * 140) * 0.94
        elif num_joinery > 80:
            price = (num_joinery * 140) * 0.9
        elif num_joinery < 40:
            price = num_joinery * 140
    elif type_joinery == "130X180":
        if 20 < num_joinery < 50:
            price = (num_joinery * 190) * 0.93
        elif num_joinery > 50:
            price = (num_joinery * 190) * 0.88
        elif num_joinery < 20:
            price = num_joinery * 190
    elif type_joinery == "200X300":
        if 25 < num_joinery < 50:
            price = (num_joinery * 250) * 0.91
        elif num_joinery > 50:
            price = (num_joinery * 250) * 0.86
        elif num_joinery < 25:
            price = num_joinery * 250
    if ways_received == "With delivery":
        price += 60
else:
    print("Invalid order")
if num_joinery > 99:
    price = price * 0.96
    print(f"{price:.2f} BGN")
elif 10 < num_joinery <= 99:
    print(f"{price:.2f} BGN")
