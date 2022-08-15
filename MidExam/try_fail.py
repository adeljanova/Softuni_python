# list_of_cards = list(map(str, input().split(", ")))
# number = int(input())
# for iteration in range(number):
#     line = input()
#     line = line.split(", ")
#     command = line[0]
#     if command == "Add":
#         card_name = line[1]
#         if card_name in list_of_cards:
#             print("Card is already in the deck")
#         else:
#             list_of_cards.append(card_name)
#             print("Card successfully added")
#     elif command == "Remove":
#         card_name = line[1]
#         if card_name in list_of_cards:
#             list_of_cards.remove(card_name)
#             print("Card successfully removed")
#         else:
#             print("Card not found")
#     elif command == "Remove At":
#         index = int(line[1])
#         if 0 <= index < len(list_of_cards):
#             list_of_cards.pop(index)
#         else:
#             print("Index out of range")
#     elif command == "Insert":
#         index = int(line[1])
#         card_name = line[2]
#         if 0 <= index < len(list_of_cards):
#             if card_name in list_of_cards:
#                 print("Card is already added")
#             else:
#                 list_of_cards.insert(index, card_name)
#                 print("Card successfully added")
#         else:
#             print("Index out of range")
#
# print(", ".join(list_of_cards))

days_number = int(input())
players_number = int(input())
group_energy = float(input())
water_perday_person = float(input())
food_perday_person = float(input())
total_water = days_number * players_number * water_perday_person
total_food = days_number * players_number * food_perday_person
condition = False
for day in range(1, days_number + 1):
    energy_loss = float(input())
    if group_energy > 0:
        group_energy -= energy_loss
    else:
        break
    if day % 2 == 0:
        group_energy += (group_energy * 0.05)
        total_water -= (total_water * 0.3)
    if day % 3 == 0:
        total_food -= (total_food / players_number)
        group_energy += (group_energy * 0.1)

    if condition:
        break
if condition:
    print(f"You are ready for the quest. You will be left with - {group_energy:.2f} energy!")
else:
    print(f"You will run out of energy. You will be left with {total_food:.2f} food and {total_water:.2f} water.")
