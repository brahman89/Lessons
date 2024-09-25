def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if  number == 0:
        return 1
    elif len(str_number) == 1:
        return first
    else:
        return first * get_multiplied_digits(int(str_number[1:]))


result = get_multiplied_digits(100008)
print(result)

result = get_multiplied_digits(40203)
print(result)

result = get_multiplied_digits(111111)
print(result)

result = get_multiplied_digits(240)
print(result)
