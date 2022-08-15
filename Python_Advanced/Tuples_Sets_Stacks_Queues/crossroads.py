from collections import deque

duration_green_light = int(input())
free_window = int(input())

cars_queue = deque()
temp_car = ''
char_hit = ''
is_hit = False
total_cars_passed = 0
data = input()
while data != "END" or is_hit:
    temp_duration = duration_green_light
    temp_free = free_window
    if data != "green":
        cars_queue.append(data)
    else:
        while len(cars_queue) > 0:
            temp_car = cars_queue.popleft()
            car_lenght = len(temp_car)
            if temp_duration == 0 and temp_free != free_window:
                break
            elif car_lenght > temp_duration:
                if car_lenght > temp_duration + free_window:
                    char_hit = temp_car[(temp_duration + free_window)]
                    is_hit = True
                    break
                else:
                    counter = 0
                    for i in range(car_lenght):
                        temp_duration -= 1
                        counter += 1
                        if temp_duration == 0:
                            break
                    car_lenght -= counter
                    temp_free -= car_lenght
                    total_cars_passed += 1
            elif car_lenght <= temp_duration:
                temp_duration -= car_lenght
                total_cars_passed += 1

        if is_hit:
            break
    data = input()

if is_hit:
    print("A crash happened!")
    print(f"{temp_car} was hit at {char_hit}.")
else:
    print("Everyone is safe.")
    print(f"{total_cars_passed} total cars passed the crossroads.")