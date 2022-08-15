class Party:
    people = []

    def __init__(self):
        self.people = []


command = input()
while command != "End":
    Party.people.append(command)
    command = input()

print(f"Going: {', '.join(Party.people)}")
print(f"Total: {len(Party.people)}")