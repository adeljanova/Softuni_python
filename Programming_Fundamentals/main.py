list_of_elements = input().split()

products = {}

for index in range(0, len(list_of_elements), 2):
    key = list_of_elements[index]
    value = list_of_elements[index + 1]
    products[index] = key
    products[index + 1] = value

print(products)

