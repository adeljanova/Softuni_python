num_of_lines = int(input())
tank_capacity = 255
filling = 0
for i in range(1, num_of_lines + 1):
    litres_of_water = int(input())
    filling += litres_of_water
    if filling > tank_capacity:
        print("Insufficient capacity!")
        filling -= litres_of_water
print(filling)

