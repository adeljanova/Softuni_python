one_lev_counter = int(input())
two_leva_counter = int(input())
five_leva_counter = int(input())
total_sum = int(input())
sum = 0
for one in range(0, one_lev_counter + 1):
    for two in range(0, two_leva_counter + 1):
        for five in range(0, five_leva_counter + 1):
            sum = one * 1 + two * 2 + five * 5
            if sum == total_sum:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {sum} lv.")