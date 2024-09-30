class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor):
        if new_floor > self.number_of_floors:
            print("Такого этажа не существует")
        else:
            for i in range(1,new_floor+1):
                print(i)


h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h3= House('Берлога', -1)
h4=House('Дупло', 99)

h1.go_to(5)
h2.go_to(10)
h3.go_to(1)
h4.go_to(2)