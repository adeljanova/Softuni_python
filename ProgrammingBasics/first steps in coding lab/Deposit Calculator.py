deposit_sum = float(input())
deposit_months = int(input())
annual_interest_percent = float(input())
interest = deposit_sum * annual_interest_percent / 100
interest_for_one_month = interest / 12
total_sum = deposit_sum  + deposit_months * interest_for_one_month
print(total_sum)