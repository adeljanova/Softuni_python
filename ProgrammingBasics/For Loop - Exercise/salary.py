open_tabs = int(input())
salary = int(input())
money_after_fine = 0
for tab in range(open_tabs):
    tab_name = input()
    if tab_name == "Facebook":
        salary -= 150
    elif tab_name == "Instagram":
        salary -= 100
    elif tab_name == "Reddit":
        salary -= 50
money_after_fine = salary
if money_after_fine <= 0:
    print("You have lost your salary.")
else:
    print(money_after_fine)