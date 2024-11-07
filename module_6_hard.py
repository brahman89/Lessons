class Figure:
    sides_count = 0

    def __init__(self, __color=(0, 0, 0), __sides=[0]):

        self.__sides = __sides
        self.__color = __color
        self.filled = True

    def get_color(self):
        return list(self.__color)

    def __is_valid_color(self, r, g, b):
        return ([r, g, b] <= [255, 255, 255] and [r, g, b] >= [0, 0, 0] and
                type(r) == int and type(b) == int and type(g) == int)

    def set_color(self, r, g, b):
        if self._Figure__is_valid_color(r, g, b) == True:
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        a = []
        b = []
        c = []

        # print(list(new_sides[0]))
        if len(list(new_sides[0])) == 1:
            if list(new_sides[0])[0] > 0 and type(list(new_sides[0])[0]) == int:
                b.append(1)
            else:
                b.append(0)
        else:

            # print(new_sides[0])
            for i in list(new_sides[0]):

                if i > 0 and type(i) == int:
                    b.append(1)
                else:
                    b.append(0)
        return all(b)

    def get_sides(self):
        if self.sides_count == 1:
            return [self.__sides]
        elif self.sides_count == 3:
            if type(self.__sides) == int:
                return [self.__sides] * self.sides_count
            else:
                return self.__sides
        elif self.sides_count == 12:
            if type(self.__sides) == int:
                return [self.__sides] * self.sides_count
            else:
                return self.__sides * self.sides_count

    def __len__(self):
        if self.sides_count == 1:  # Длина окружности 2*пи*R
            return self.__sides

        else:
            return sum(self.get_sides())

    def set_sides(self, *new_sides):

        # print(len(new_sides))

        if len(list(new_sides)) == 1:
            if self._Figure__is_valid_sides(new_sides) == True:
                # print(new_sides)
                self.__sides = list(new_sides)[0]
        elif len(list(new_sides)) == 12:  # в кубе все стороны должны быть равны
            for i in range(12):
                if list(new_sides)[i] == list(new_sides)[i - 1]:
                    self.__sides = [list(new_sides)[0]]
        else:
            # print(len(new_sides))
            if self.sides_count == len(new_sides) and self._Figure__is_valid_sides(new_sides) == True:
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, __colour, __sides):
        Figure.__init__(self, __colour, __sides)

        __radius = (float(self.get_sides()[0])) * (1.0 / (2.0 * 3.14))

        # print(__radius)

    def get_square(self):
        __radius = (float(self.get_sides()[0])) * (1.0 / (2.0 * 3.14))
        return (3.14 * float((__radius) * (__radius)))


class Triangle(Figure):
    sides_count = 3

    def __init__(self, __colour, __sides):
        Figure.__init__(self, __colour, __sides)

    def get_square(self):
        p = self.__len__() / 2
        a = triangle1.get_sides()
        s = p * (p - a[0]) * (p - a[1]) * (p - a[2])
        return (float(s) ** 0.5)


class Cube(Figure):
    sides_count = 12

    def __init__(self, __colour, __sides):
        Figure.__init__(self, __colour, __sides)

    def get_volume(self):
        return self.get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())



""" Проверки
# f = Figure()
#
# f.set_sides(1, 2, 3)
#
# print(f._Figure__sides)
# print(f._Figure__is_valid_sides(1, 2, 3))
#
# # print(len(f._Figure__sides))
#
# # f.get_sides()
# #
# # print(f.__len__())
# #
# #


# circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
# cube1 = Cube((222, 35, 130), 6)
# print(circle1.__dir__())
# # # # Проверка на изменение цветов:
# # circle1.set_color(55, 66, 77)  # Изменится
# # print(circle1.get_color())
# # cube1.set_color(300, 70, 15)  # Не изменится
# # print(cube1.get_color())
# #
# # # Проверка на изменение сторон:
# cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
# cube1.set_sides(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)  # можем задать каждую сторону куба
# # cube1.set_sides(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
# print(cube1.get_sides())
# circle1.set_sides(1, 5)
# circle1.set_sides(15)  # Изменится
# print(circle1.get_sides())
# # print(cube1.__len__())
#
# # print(circle1._Figure__is_valid_sides(-1))
#
# #
# # # Проверка периметра (круга), это и есть длина:
# print(circle1.__len__())
# #
# # # Проверка объёма (куба):
# print(cube1.get_volume())
# # # Проверка площадь круга
# # print(f'\n')
# print(circle1.get_square())
# # # Проверка треугольника
# # print(f'\n')
# # triangle1 = Triangle((1, 2, 3), 3)
# # print(triangle1.get_sides())
# # triangle1.set_sides(5, 3)  # не примет
# # print(triangle1.get_sides())
# # # triangle1.set_sides(5, 3, 4)  # не примет
# # print(triangle1.get_sides())
# #
# # print(triangle1.__len__())  # периметр
# # print(triangle1.get_square())#площадь треугольника
"""
