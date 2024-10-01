class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print("Такого этажа не существует")
        else:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        print(f'Название: {self.name}, кол-во этажей: {self.number_of_floors}.')


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3 = House('Берлога', 1)
h4 = House('Дупло', 99)

# __str__
h1.__str__()
h2.__str__()
h3.__str__()
h4.__str__()

# __len__
print(len(h1))
print(len(h2))
print(len(h3))
print(len(h4))
