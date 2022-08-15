text = input()
final = []
for i in range(len(text)):
    if final:
        if text[i] != final[-1]:
            final.append(text[i])
    else:
        final.append(text[i])
print("".join(final))