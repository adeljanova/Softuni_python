# pairs = input().split()
#
# searched_products = input().split()
#
# bakery = {}
# for i in range(0, len(pairs), 2):
#     key = pairs[i]
#     value = pairs[i+1]
#     bakery[key] = int(value)
#
# for product in searched_products:
#     if product in bakery:
#         print(f"We have {bakery[product]} of {product} left")
#     else:
#         print(f"Sorry, we don't have {product}")

info = input().split(" ")
bakery = dict()

for i in range(0, len(info), 2):
    key = info[i]
    value = info[i + 1]
    bakery[key] = int(value)

check = input().split(" ")
for item in check:
    if item in bakery:
        print(f"We have {bakery[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")
