s = []
def calculate_structure_sum(data):
    global s
    if data==0:
        s.append(data)
    elif type(data) == int:
        s.append(data)
    elif type(data) == str:
        s.append(len(data))
    elif type(data) == list:
        for i in data:
            calculate_structure_sum(i)
    elif type(data) == tuple:
        for j in data:
            calculate_structure_sum(j)
    elif type(data) == dict:
        d = list(data.items())
        for k in d:
            calculate_structure_sum(k)
    elif type(data) == set:
        for l in data:
            calculate_structure_sum(l)
    return sum(s)


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",((), [{(2, 'Urban', ('Urban2', 35))}])]
result = calculate_structure_sum(data_structure)
print(result)
