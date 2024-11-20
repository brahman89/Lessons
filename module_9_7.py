def is_prime(func):
    def wrapper(*args, **kwargs):
        m = []
        result = func(*args, **kwargs)
        for i in range(2, result + 1):
            if result % i == 0:
                m.append(1)
        # print(result)
        # print(len(m))
        if len(m) > 2:
            print("Составное")
        else:
            print("Простое")
        return result

    return wrapper


@is_prime
def sum_three(*args):
    return sum(args)


result = sum_three(2, 3, 6)
print(result)
