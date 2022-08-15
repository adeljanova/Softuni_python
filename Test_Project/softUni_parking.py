n = int(input())

parking = {}

for iteration in range(n):
    command = input().split()
    registration = command[0]
    username = command[1]
    if registration == "register":
        license_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_number}")
        else:
            parking[username] = license_number
            print(f"{username} registered {license_number} successfully")
    elif registration == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            del parking[username]
            print(f"{username} unregistered successfully")

output = [print(f"{key} => {value}") for key, value in parking.items()]


