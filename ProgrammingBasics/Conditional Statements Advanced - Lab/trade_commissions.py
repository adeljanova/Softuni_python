city = input()
quantity = float(input())
commision = 0
tramp = True
if city == "Sofia" and tramp:
    if 0 <= quantity <= 500:
        commision = quantity * 0.05
    elif 500 < quantity <= 1000:
        commision = quantity * 0.07
    elif 1000 < quantity <= 10000:
        commision = quantity * 0.08
    elif quantity > 10000:
        commision = quantity * 0.12
    else:
        tramp = False
elif city == "Varna" and tramp:
    if 0 <= quantity <= 500:
        commision = quantity * 0.045
    elif 500 < quantity <= 1000:
        commision = quantity * 0.075
    elif 1000 < quantity <= 10000:
        commision = quantity * 0.10
    elif quantity > 10000:
        commision = quantity * 0.13
    else:
        tramp = False
elif city == "Plovdiv" and tramp:
    if 0 <= quantity <= 500:
        commision = quantity * 0.055
    elif 500 < quantity <= 1000:
        commision = quantity * 0.08
    elif 1000 < quantity <= 10000:
        commision = quantity * 0.12
    elif quantity > 10000:
        commision = quantity * 0.145
    else:
        tramp = False
else:
    tramp = False
if tramp:
    print(f"{commision:.2f}")
else:
    print("error")