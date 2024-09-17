import random
random_value = random.randint(3,20)
password = ""
for i in range(1, random_value):
    for j in range(i+1, random_value):
        if random_value % (i + j) == 0:
            password += f'{i}{j}'
#print(password)
print(f'{random_value} - {password}')
print('20 - 13141911923282183731746416515614713812911')#для проверки