string_of_names = input().split()
palindrome = input()

reversed_palindrome = ""
counter = 0
new_list = []
for i in string_of_names:
    reversed_list = reversed(i)
    reversed_palindrome = "".join(reversed_list)
    if i == reversed_palindrome:
        new_list.append(reversed_palindrome)
        if reversed_palindrome == palindrome:
            counter += 1
print(new_list)
print(f"Found palindrome {counter} times")
