data = input()

dwarf_dict = {}

while data != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = data.split(" <::> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_name not in dwarf_dict:
        dwarf_dict[dwarf_name] = {}
    if dwarf_hat_color not in dwarf_dict[dwarf_name]:
        dwarf_dict[dwarf_name][dwarf_hat_color] = dwarf_physics
    else:
        pass