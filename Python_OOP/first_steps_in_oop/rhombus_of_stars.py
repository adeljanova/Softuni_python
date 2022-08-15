def get_rhombus(n):
    for i in range(n):
        print(" " * (n - i - 1) + "* " * (i + 1))

    for j in range(n - 2, -1, -1):
        print(" " * (n - j - 1) + "* " * (j + 1))


n = int(input())
get_rhombus(n)
