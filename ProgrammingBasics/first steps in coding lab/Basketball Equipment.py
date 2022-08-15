annual_tax_for_basketball = int(input())
sneackers = annual_tax_for_basketball - (annual_tax_for_basketball * 4 / 10)
tracksuit = sneackers - (sneackers * 1 / 5)
ball = tracksuit * (1 / 4)
accessories = ball * (1 / 5)
total_price = annual_tax_for_basketball + sneackers + tracksuit + ball + accessories
print(total_price)