company = input()
tickets_elderly = int(input())
tickets_children = int(input())
net_price_elderly = float(input())
tax = float(input())
net_price_children = net_price_elderly * 0.3
elderly_tax = net_price_elderly + tax
children_tax = net_price_children + tax
total_price = (tickets_elderly * elderly_tax) + (tickets_children * children_tax)
profit = total_price * 0.2
print(f"The profit of your agency from {company} tickets is {profit:.2f} lv.")