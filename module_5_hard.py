'''Свой YouTube'''
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'{self.nickname},{self.password},{self.age}'


# a=User('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# a1=User('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
# print(a,a1, sep="\n")

class Video:
    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

        '''adult_mode=True 18+'''

    def __str__(self):
        return f'{self.title},  {self.duration}, {self.time_now}, {self.adult_mode}'


# v1 = Video('Лучший язык программирования 2024 года', 200)
# v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
# print(v1, v2 ,sep="\n")

class UrTube:
    users = []
    videos = []
    current_user = None

    def log_in(self, nickname, password):

        for i in UrTube.users:
            if nickname==(str(i).split(",")[0]) and hash(password)==hash(str(i).split(",")[1]):
                UrTube.current_user=f'{nickname},{i.split(",")[2]}'
        # print(UrTube.current_user)

    def register(self, nickname, password, age):
        for i in UrTube.users:
            if nickname==str(i).split(",")[0]:
                print(f"Пользователь {nickname} уже существует")
            else:
                continue
        UrTube.users.append(str(f'{nickname},{password},{age}'))
        UrTube.log_in(User, f'{nickname}',f'{password}')
        # print(str(UrTube.users).split(",")[0],str(UrTube.users).split(",")[1])


    def log_out(self):
        current_user = None

    def add(self, *args):
        for i in args:
            UrTube.videos.append(str(i))
            # print(i)

    def get_videos(self, word):
        search_list=[]
        for i in UrTube.videos:
            # print(i)
            if str(word).lower() in (str(i).split(",")[0]).lower():
                search_list.append(str(i).split(",")[0])
        return search_list



    def watch_video(self, video):
        if UrTube.current_user==None:
            print("Войдите в аккаунт, чтобы смотреть видео")
        elif int(str(UrTube.current_user).split(",")[1])<18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
        else:
            for i in UrTube.videos:
                if video==(str(i).split(",")[0]):
                    for j in range(int(str(i).split(",")[1])):
                        print(j, end=" ")
                        time.sleep(1)
                    print("Конец видео")

    def __str__(self):
        # for i in UrTube.videos:
        return f"{UrTube.videos}, {UrTube.users}"


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
