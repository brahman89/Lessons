'''соперничество двух команд - Мастера кода и Волшебники данных'''

team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

'''Использование %'''
print("В команде Мастера кода участников: %s !" % team1_num)
print("В команде Волшебники данных участников: %s !" % team2_num)
print("Итого сегодня в командах участников: %s и %s !" % (team1_num, team2_num))
print("\n")

'''Использование format()'''
print("Команда Волшебники данных решила задач: {0} !\n"
      "Команда Мастера кода решила задач: {1} !\n"
      "Волшебники данных решили задачи за {2} c!\n"
      "Мастера кода решили задачи за {3} c!".format(score_2, score_1, team2_time, team1_time))
print("\n")

'''Использование f-строк'''
print(f'Команды решили {score_1} и {score_2} задач.')

if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
    result = "Победа команды Мастера кода!"
elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
    result = "Победа команды Волшебники Данных!"
else:
    result = "Ничья!"
print(f'Результат битвы: победа команды {result}!')
print(
    f'Сегодня было решено {score_1 + score_2} задач, в среднем по {round((team2_time + team1_time) / (score_1 + score_2), 1)} секунды на задачу!')
