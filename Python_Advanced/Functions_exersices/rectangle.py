def rectangle(*args):
    if type(args[0]) == int and type(args[1]) == int:

        def area(len, wid):
            rectangle_area = len * wid
            return rectangle_area

        def perimeter(len, wid):
            rectangle_perimeter = len * 2 + wid * 2
            return rectangle_perimeter

    else:
        return "Enter valid values!"

    return f"Rectangle area: {area(*args)}\nRectangle perimeter: {perimeter(*args)}"


print(rectangle(2, 10))
print(rectangle('2', 10))
