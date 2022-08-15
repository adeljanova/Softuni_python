M = int(input())
counter = 0
flag = False
a = 1
b = 1
c = 1
d = 1
password = ""
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if a < b:
                    if c > d:
                        if a * b + c * d == M:
                            print(f"{a}{b}{c}{d}", " ", end="")
                            counter += 1
                            if counter == 4:
                                password = str(a) + str(b) + str(c) + str(d)

if counter < 4:
    print("No!")
else:
    print(f"Password: {password}")