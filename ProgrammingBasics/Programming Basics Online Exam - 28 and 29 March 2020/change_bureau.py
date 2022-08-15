num_bitcoin = int(input())
num_china = float(input())
commission_percent = float(input())
sum_bitcoin = num_bitcoin * 1168
dollar = 1.76
sum_china = num_china * 0.15 * dollar
total = (sum_china + sum_bitcoin) / 1.95
commission = commission_percent / 100 * total
total_sum = total - commission
print(f"{total_sum:.2f}")