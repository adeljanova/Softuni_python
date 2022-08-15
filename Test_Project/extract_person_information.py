lines = int(input())

name = ''
age = ''
for i in range(lines):
    data = input().split("@")
    usable = data[1].split("|")
    name = usable[0]
    leftover = usable[1].split("#")
    final_bit = leftover[1].split("*")
    age = final_bit[0]
    print(f"{name} is {age} years old.")



