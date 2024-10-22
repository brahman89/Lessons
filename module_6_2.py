class Vehicle:
    __COLOR_VARIANTS = ['purple', 'rouge', 'green_grass', 'black', 'white_snow']

    def __init__(self, owner, __model, __color, __engine_power):
        self.owner = owner
        self.__model = __model
        self.__engine_power = __engine_power
        self.__color = __color

    def get_model(self):
        return f"Модель: {self.__model}"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}"

    def get_color(self):
        return f"Цвет: {self.__color}"

    def print_info(self):
        print(f"{self.get_model()} \n{self.get_horsepower()} \n{self.get_color()} \nВладелец: {self.owner}")

    def set_color(self, new_color):

        if str(new_color).lower() in self._Vehicle__COLOR_VARIANTS:
            self.__color = new_color
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5


# __COLOR_VARIANTS = ['purple', 'rouge', 'green_grass', 'black', 'white_snow']
vehicle1 = Sedan('Fedos', 'Toyota Mark II', 'purple', 500)

# Изначальные свойства
vehicle1.print_info()

# Меняем свойства (в т.ч. вызывая методы)
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'

# Проверяем что поменялось
vehicle1.print_info()
