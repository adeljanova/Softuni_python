lenght_sm = int(input())
width_sm = int(input())
height_sm = int(input())
percent_occupied = float(input())
volume_of_the_aquarium = lenght_sm * width_sm * height_sm
volume_in_litres = volume_of_the_aquarium / (10 * 10 * 10)
needed_litres = volume_in_litres * (1 - (percent_occupied / 100))
print(needed_litres)