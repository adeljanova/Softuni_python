fires_with_their_cells = input().split("#")
water = int(input())
effort = 0
total_fire = 0
new_list = []
final_list = []
for index in fires_with_their_cells:
    temp_fires_with_their_cells = index.split("=")
    type_of_fire = temp_fires_with_their_cells[0]
    value_of_cell = int(temp_fires_with_their_cells[1])
    if water >= value_of_cell:
        if "High" in type_of_fire:
            if 81 <= value_of_cell <= 125:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                new_list.append(f"- {value_of_cell}")
        elif "Medium" in type_of_fire:
            if 51 <= value_of_cell <= 80:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                new_list.append(f"- {value_of_cell}")
        elif "Low" in type_of_fire:
            if 1 <= value_of_cell <= 50:
                water -= value_of_cell
                effort += value_of_cell * 0.25
                total_fire += value_of_cell
                new_list.append(f"- {value_of_cell}")
final_list = "\n".join(new_list)
print("Cells:", end="\n")
print(final_list)
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")






