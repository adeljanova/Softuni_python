class sequence_repeat:

    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):

        while self.number > 0:
            self.number -= 1
            if self.index >= len(self.sequence):
                self.index = 1
            else:
                self.index += 1

            return self.sequence[self.index-1]

        raise StopIteration()


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
