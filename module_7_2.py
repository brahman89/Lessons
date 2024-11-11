import io


def custom_write(file_name, strings):
    file_name = "text.txt"
    strings_positions = {}
    with open(file_name, "w+", encoding="utf-8") as file:
        k = 0
        for i in strings:
            k += 1
            # print(file.tell())
            file.write(str(i) + "\n")
            strings_positions[(k, file.tell())] = str(i)

    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!',
    'Пожалуйста!'
]

result = custom_write('test.txt', info)
for elem in result.items():
    print(elem)
