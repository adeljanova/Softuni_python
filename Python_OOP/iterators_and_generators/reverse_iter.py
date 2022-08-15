
class reverse_iter:
    def __init__(self, numbers):
        self.numbers = list(numbers)

    def __iter__(self):
        return self

    def __next__(self):
        for _ in range(len(self.numbers)):
            return self.numbers.pop()

        raise StopIteration()


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
