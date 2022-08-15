from math import floor
number_of_pages_of_a_book = int(input())
pages_for_one_hour = int(input())
number_of_days = int(input())
time_to_read_a_book = number_of_pages_of_a_book / pages_for_one_hour
needed_hours_per_day = time_to_read_a_book / number_of_days
print(floor(needed_hours_per_day))