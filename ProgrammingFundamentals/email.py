class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def sent(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: " \
               f"{self.content}. Sent: {self.is_sent}"


line = input()

emails = []
while line != "Stop":
    line = line.split()
    sender = line[0]
    receiver = line[1]
    content = line[2]
    email = Email(sender, receiver, content)
    emails.append(email)
    line = input()

indices = list(map(int, input().split(", ")))

for i in indices:
    emails[i].sent()

for email in emails:
    print(email.get_info())
