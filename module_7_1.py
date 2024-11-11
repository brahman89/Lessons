class Product:

    def __init__(self, name='', weight=0.0, category=''):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop(Product):
    __file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name) as file:
            text = file.read()
            return text

    def add(self, *products):
        with open(self.__file_name) as file:
            text = file.read()
            for i in list(products):
                # print(str(i).partition(', ')[0])
                if str(i).partition(', ')[0] in text:
                    print(f"Продукт {str(i)} уже есть в магазинe")
                else:
                    file.write(str(i) + "\n")


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
