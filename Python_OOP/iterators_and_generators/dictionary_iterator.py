class dictionary_iter:

    def __init__(self, dict: dict):
        self.dict = list(dict.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        while self.index < len(self.dict):
            value_to_return = self.dict[self.index]
            self.index += 1
            return value_to_return

        raise StopIteration


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
