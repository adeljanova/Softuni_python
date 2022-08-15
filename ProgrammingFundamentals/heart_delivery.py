string_of_even_integers = list(map(int, input().split("@")))
house_counter = len(string_of_even_integers)

command = input()

index = 0
new_index = 0
final_house_counter = 0
while command != "Love!":
    is_celebrating = False
    command = command.split()
    jump = int(command[1])

    for index in range(0, house_counter + 1, jump):
        if index > house_counter:
            index = 0
            string_of_even_integers[index] -= 2
            if string_of_even_integers[index] < 0:
                string_of_even_integers[index] = 0
        else:
            string_of_even_integers[index] -= 2
            if string_of_even_integers[index] < 0:
                string_of_even_integers[index] = 0
        if string_of_even_integers[index] == 0:
            is_celebrating = True
            print(f"Place {index} has Valentine's day.")
            break

    if is_celebrating:
        print(f"Place {index} already had Valentine's day.")

    command = input()
print(f"Cupid's last position was {index}.")
for house in range(len(string_of_even_integers)):
    if string_of_even_integers[house] == 0:
        final_house_counter += 1

if final_house_counter == house_counter:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {house_counter - final_house_counter} places.")

