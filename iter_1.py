class MyRange:

    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end

    def __iter__(self):
        print('Вход в цикл')
        self.cursor = self.start - 1
        return self

    def __next__(self):
        self.cursor += 1

        if self.cursor >= self.end:
            print('Конец цикла')
            raise StopIteration
        
        return self.cursor


for item in MyRange(4, 20):
    print(item)
