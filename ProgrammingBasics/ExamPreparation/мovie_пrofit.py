movie = input()
num_days = int(input())
num_tickets = int(input())
price_ticket = float(input())
percent_cinema = int(input())
sum_tickets_for_day = num_tickets * price_ticket
total_sum = sum_tickets_for_day * num_days
total_sum -= total_sum * percent_cinema / 100
print(f"The profit from the movie {movie} is {total_sum:.2f} lv.")