from math import pi
geometric_figure = input()
if geometric_figure == "square":
    side_lenght_of_square = float(input())
    area_of_square = side_lenght_of_square * side_lenght_of_square
    print(f"{area_of_square:.3f}")
elif geometric_figure == "rectangle":
    small_side = float(input())
    big_side = float(input())
    area_of_rectangle = small_side * big_side
    print(f"{area_of_rectangle:.3f}")
elif geometric_figure == "circle":
    radius = float(input())
    area_of_circle = pi * radius * radius
    print(f"{area_of_circle:.3f}")
elif geometric_figure == "triangle":
    side_lenght_of_triangle = float(input())
    h_lenght = float(input())
    area_of_triangle = (side_lenght_of_triangle * h_lenght) / 2
    print(f"{area_of_triangle:.3f}")