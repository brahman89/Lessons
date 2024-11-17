first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (abs(x[0] - x[1]) for x in zip(list(map(len, first)), list(map(len, second))) if abs(x[0] - x[1]) != 0)
second_result = (len(first[i]) == len(second[i]) for i in range(len(first)))

# second_result = ( list(map(len, first + second)))
# print(list(map(len, first)))
# print(list(map(len, second)))

# как это сжать в строку блин
#
# f=[]
# for i in range(len(first)):
#     if len(first[i])==len(second[i]):
#         f.append(True)
#     else:
#         f.append(False)
# print(f)


print(list(first_result))
print(list(second_result))
