import requests
import sys
from PIL import Image, ImageDraw
import matplotlib.pyplot as plt
import matplotlib.patheffects as fx
import numpy as np

'''применение библиотеки  requests'''
#
# for url in ['https://vandal.sdf-eu.org/JapaneseGuide/index.html',
#             'https://en.wikipedia.org/wiki/Overlord_(novel_series)', 'https://store.steampowered.com/']:
#     response = requests.get(url, stream=True)
#
#     # код состояния
#     print(f'HTTP-код состояния адреса {url} - ',response.status_code)
#     # HTTP заголовки ответов на запрос
#
#     print(response.headers)
#     print(response.headers['server'])
#
#     # кодировка содержимого данных с сервера
#     print(response.encoding)
#
#     print(response.raw.read(10))
#
#     # перевод информации из байтового вида в строковый
#     # print(response.text)


'''применение библиотеки  matplotlib'''

# # построение линий
# fig, ax = plt.subplots()
# ax.plot([1, 2, 3, 4], [1, 4, 2, 3])
# plt.show()

# # построение синусоиды
# X = np.linspace(0, 10*np.pi, 1000)
# Y = np.sin(X)
# fig, ax = plt.subplots()
# ax.plot(X, Y)
# plt.show()

# # построение пораболы
# X=np.arange(-100,100)
# Y=X**2
# fig, ax = plt.subplots()
# ax.plot(X, Y)
# #аннотация
# ax.annotate("A", (X[50],Y[50]), (X[50],20), ha="center", va="center", arrowprops={"arrowstyle": "->", "color": "C3"})
# plt.show()

# # точечная диаграмма
# X = np.random.uniform(0, 1, 100)
# Y = np.random.uniform(0, 1, 100)
# fig, ax = plt.subplots()
# ax.scatter(X, Y)
# plt.show()
#
# # построение столбчатой диаграммы
# X = np.arange(10)
# Y = np.random.uniform(1, 10, 10)
# fig, ax = plt.subplots()
# ax.bar(X, Y)
# plt.show()
#
# # построение мозаичной диаграммы
#
# Z = np.random.uniform(0, 1,  (8, 8))
# fig, ax = plt.subplots()
# text = ax.text(0.5, 0.5, "Mazaik")
# text.set_path_effects([fx.Stroke(linewidth=6, foreground="1.0"), fx.Normal()])
# ax.imshow(Z)
# plt.show()

'''применение библиотеки  pillow'''
#
with Image.open("im3.jpg") as im:
    image = im.resize((640, 480))
    image.show()
    image.save("im3_1.jpg")
#
#
#изменение цвета в ч\б
with Image.open("im2.jpg") as im:
    image = im.convert('L')
    image.save("im2.jpg")
    image.show()
#
#
# # рисование креста на картинке
with Image.open("hopper.jpg") as im:
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=256)
    draw.line((0, im.size[1], im.size[0], 0), fill=256)
    im.show()
    im.save("hopper.jpg",format="png")


