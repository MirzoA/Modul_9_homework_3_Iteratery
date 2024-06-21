class EvenNumbers:
    def __init__(self, start = 0, end = 1):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            while self.start % 2 != 0:
                self.start += 1
            result = self.start
            self.start += 2
            return result
        else:
            raise StopIteration()  # признак того, что больше возвращать нечего


en = EvenNumbers(10, 25)
for i in en:
    print(i)