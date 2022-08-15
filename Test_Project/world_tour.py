stops = input()
data = input()

while data != "Travel":
    split_data = data.split(":")
    command = split_data[0]
    if command == "Add Stop":
        index = int(split_data[1])
        string = split_data[2]
        if index < len(stops):
            stops = stops[:index] + string + stops[index:]
        print(stops)
    elif command == "Remove Stop":
        start_index = int(split_data[1])
        end_index = int(split_data[2])
        if start_index < len(stops) and end_index < len(stops):
            stops = stops[:start_index] + stops[end_index+1:]
        print(stops)
    elif command == "Switch":
        old_string = split_data[1]
        new_string = split_data[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
        print(stops)
    data = input()

print(f"Ready for world tour! Planned stops: {stops}")