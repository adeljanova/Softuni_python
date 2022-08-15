version = input().split(".")
version_number = int("".join(version)) + 1

new_version = [str(i) for i in str(version_number)]
print(".".join(new_version))