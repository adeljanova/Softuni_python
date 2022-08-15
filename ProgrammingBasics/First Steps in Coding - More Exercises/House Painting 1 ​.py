x = float(input())
y = float(input())
h = float(input())
front_wall = (x * x) - (1.2 * 2)
back_wall = x * x
side_walls = (x * y) - (1.5 * 1.5)
front_roof = (x * h) / 2
side_roof = x * y
green_paint_for_one_litre = 3.4
red_paint_for_one_litre = 4.3
total_area_walls = front_wall + back_wall + (2 * side_walls)
total_area_roof = (front_roof * 2) + (side_roof * 2)
needed_green_paint = total_area_walls / green_paint_for_one_litre
needed_red_paint = total_area_roof / red_paint_for_one_litre
print(f"{needed_green_paint:.2f}")
print(f"{needed_red_paint:.2f}")
