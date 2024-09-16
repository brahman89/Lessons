import random
random_value = random.randint(3,20)
password = ""
for i in range(1, random_value):
    for j in range(i, random_value):
        if random_value % (i + j) == 0:
            password += f'{str(i)} + {str(j)}  '
#print(password)
print(f'{random_value} - {password}')