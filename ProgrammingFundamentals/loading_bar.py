def loading_bar_view(number):
    digit = number // 100
    if number == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        print(f"{number}% [{((number // 10) * '%') + (10 - (number // 10)) * '.'}]")
        print("Still loading...")


declared_number = int(input())
loading_bar_view(declared_number)
