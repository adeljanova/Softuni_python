data = input()

username_storage = {}
submissions = {}

while data != "exam finished":
    command = data.split("-")
    username = command[0]
    language = command[1]
    if language == "banned":
        del username_storage[username]
    else:
        points = int(command[2])
        if username not in username_storage:
            username_storage[username] = points
        else:
            if username_storage[username] < points:
                username_storage[username] = points
        if language not in submissions:
            submissions[language] = 0
        submissions[language] += 1
    data = input()

print("Results:")
output_1 = [print(f"{key} | {value}") for key, value in username_storage.items()]
print("Submissions:")
output_2 = [print(f"{key} - {value}") for key, value in submissions.items()]



