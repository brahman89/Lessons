print('Введите три числа ниже')
first = input("Первое число :")
second = input("Второе число :")
third = input("Третье число :")
if first==second and second==third:
    print(3)
elif first == second or second == third:
    print(2)
else:
    print(1)