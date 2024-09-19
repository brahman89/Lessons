def print_params(a=1, b='строка', c=True):
    print(a, b, c)

#1
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])
#2
print("\n")
values_list = ['sdf', False, 123]
values_dict = {"a": "Pi", "b": 180, "c": "sdf"}
print_params(*values_list)
print_params(**values_dict)
#3
print("\n")
values_list_2=[(1,5,"fg"),0.156]
print_params(*values_list_2, 42)
