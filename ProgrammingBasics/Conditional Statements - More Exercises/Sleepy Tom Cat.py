number_of_rested_days = int(input())

time_to_play_with_tom = 30000
days_of_the_year_working = 365 - number_of_rested_days
when_at_work = days_of_the_year_working * 63
when_he_rests = number_of_rested_days * 127
total_play_time = when_at_work + when_he_rests
if time_to_play_with_tom < total_play_time:
    time_left = total_play_time - time_to_play_with_tom
    hours_left = time_left // 60
    minutes_left = time_left % 60
    print(f"Tom will run away")
    print(f"{hours_left} hours and {minutes_left} minutes more for play")
elif time_to_play_with_tom >= total_play_time:
    time_over = time_to_play_with_tom - total_play_time
    hours_over = time_over // 60
    minutes_over = time_over % 60
    print(f"Tom sleeps well")
    print(f"{hours_over} hours and {minutes_over} minutes less for play")

