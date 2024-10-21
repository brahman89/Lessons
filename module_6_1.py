class Animal:

    def __init__(self, name1):
        self.name1 = name1
        self.alive = True
        self.fed = False


class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False


class Mammal(Animal):

    def eat(self, food):
        food is Plant.__call__(self)
        if food.edible == True:
            print(f"{self.name1} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name1} не стал есть {food.name}")
            Animal.alive = False


class Predator(Animal):

    def eat(self, food):
        food is Plant.__call__(self)
        if food.edible == True:
            print(f"{self.name1} съел {food.name}")
            Animal.fed = True
        else:
            print(f"{self.name1} не стал есть {food.name}")
            Animal.alive = False


class Flower(Plant):
    Plant.edible = False


class Fruit(Plant):
    Plant.edible = True


a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name1)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
