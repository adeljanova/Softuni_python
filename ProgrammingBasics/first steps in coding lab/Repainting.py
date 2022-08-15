price_for_bag = 0.40
needed_nylon = int(input())
needed_paint = int(input())
needed_dividers = int(input())
hours_for_doing_the_work = int(input())
total_price_for_nylon = (needed_nylon + 2) * 1.50
total_price_for_paint = (needed_paint + (needed_paint * (10 / 100))) * 14.50
total_price_for_dividers = needed_dividers * 5.00
total_sum = total_price_for_paint + total_price_for_dividers + total_price_for_nylon + price_for_bag
total_sum_for_craftsman = (total_sum * 30 /100) * hours_for_doing_the_work
end_sum = total_sum_for_craftsman + total_sum
print(end_sum)


