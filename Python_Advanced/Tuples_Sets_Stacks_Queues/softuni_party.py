num_of_guests = int(input())
guest_list = set()

for _ in range(num_of_guests):
    person = input()
    guest_list.add(person)

output = []
data = input()
while data != "END":
    if data in guest_list:
        guest_list.remove(data)
    data = input()

vip = set()
regular = set()
for guest in guest_list:
    if guest[0].isdigit():
        vip.add(guest)
    else:
        regular.add(guest)
print(len(guest_list))
[print(guest) for guest in sorted(vip)]
[print(guest) for guest in sorted(regular)]

