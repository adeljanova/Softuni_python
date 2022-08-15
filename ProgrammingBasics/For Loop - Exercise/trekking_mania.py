number_of_groups = int(input())
Musala = 0
Monblan = 0
Kilimandzharo = 0
K2 = 0
Everest = 0
total_people = 0
sum_musala = 0
sum_monblan = 0
sum_kilimandzharo = 0
sum_k2 = 0
sum_everest = 0
for i in range(number_of_groups):
    num_of_people_in_each_group = int(input())
    total_people += num_of_people_in_each_group
    if num_of_people_in_each_group < 6:
        sum_musala += num_of_people_in_each_group
    elif 5 < num_of_people_in_each_group < 13:
        sum_monblan += num_of_people_in_each_group
    elif 12 < num_of_people_in_each_group < 26:
        sum_kilimandzharo += num_of_people_in_each_group
    elif 25 < num_of_people_in_each_group < 41:
        sum_k2 += num_of_people_in_each_group
    else:
        sum_everest += num_of_people_in_each_group
Musala = sum_musala / total_people * 100
Monblan = sum_monblan / total_people * 100
Kilimandzharo = sum_kilimandzharo / total_people * 100
K2 = sum_k2 / total_people * 100
Everest = sum_everest / total_people * 100
print(f"{Musala:.2f}%")
print(f"{Monblan:.2f}%")
print(f"{Kilimandzharo:.2f}%")
print(f"{K2:.2f}%")
print(f"{Everest:.2f}%")