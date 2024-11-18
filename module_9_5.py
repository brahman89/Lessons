class StepValueError(ValueError):
    def __str__(self):
        return 'шаг не может быть равен 0'

class Iterator:

    def __init__(self, start, stop, step=1):

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = 0
        if self.step == 0:
            raise StepValueError()

    def __iter__(self):
        self.pointer = self.start
        return self

    def __next__(self):
        self.pointer = self.start
        self.start += self.step
        if self.step > 0:
            if self.pointer > self.stop:
                raise StopIteration()
        if self.step < 0:
            if self.pointer < self.stop:
                raise StopIteration()
        return self.pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print('Шаг указан неверно')

iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')

# print("Шаг указан неверно\n-5 -4 -3 -2 -1 0 1\n6 8 10 12 14\n5 4 3 2 1")
