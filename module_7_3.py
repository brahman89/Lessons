from operator import index


class WordsFinder:
    file_names = []

    def __init__(self, *files):
        for i in files:
            self.file_names.append(i)

        # print(self.file_names)

    def get_all_words(self):
        all_words = {}

        for k in self.file_names:

            with open(k, encoding="utf-8") as file:
                text_list = []
                lower_text = file.read().lower()
                simbols = [',', '.', '=', '!', '?', ';', ':', ' - ', '\n']
                # print(lower_text)
                pre_text = []
                for i in lower_text:
                    if i in simbols:
                        pre_text.append("@")
                    else:
                        pre_text.append(i)
                solved_text = []
                solved_text.append("".join(pre_text))
                a = str(solved_text[0]).replace("@@", " ")
                a = str(solved_text[0]).replace("@", " ")
                for i in a.split():
                    text_list.append(i)
                # print(text_list)

                all_words[k] = text_list

        return all_words

    def find(self, word=""):
        find = {}
        word = word.lower()
        for k in self.get_all_words().items():
            # print(k)
            if word in k[1]:
                find[k[0]] = k[1].index(word) + 1
        return find

    def count(self, word=""):
        count = {}
        word = word.lower()
        for k in self.get_all_words().items():
            if word in k[1]:
                count[k[0]] = k[1].count(word)
        return count


finder2 = WordsFinder('test_file.txt', 'test_file2.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего

# старый пример
# finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt', 'Rudyard Kipling - If.txt',
#                       'Mother Goose - Monday’s Child.txt')
# print(finder1.get_all_words())
# print(finder1.find('thE'))
# print(finder1.count('tHe'))
