string = input().split("|")
string.reverse()
output = []
for str in string:
    output.append(str.split())
[print(output[i][j], end=" ") for i in range(len(output)) for j in range(len(output[i]))]