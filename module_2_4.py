Primes = []
Not_Primes = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
for num in range(2, len(numbers) + 1):
    for ind in range(2, len(numbers) + 1):
        if (num / ind - num // ind) == 0 and num != ind and num / ind >= 1:
            Not_Primes.append(num)
            break
    else:
        Primes.append(num)

print("Primes :", list(set(Primes)))
print("Not_Primes:", list(set(Not_Primes)))

