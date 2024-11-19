# '''работа цикла (как из этого сделать ГЕНЕРАТО?)'''
# text = "abc"
# k = 0
# i = 0
# while True:
#     if i < 3:
#         i += 1
#         print(text[k:i])
#         # print(k, i)
#         k += 1
#     else:
#         break
# k = 0
# i = 1
# while True:
#     if i < 3:
#         i += 1
#         print(text[k:i])
#         # print(k, i)
#         k += 1
#     else:
#         break
# k = 0
# i = 2
# while True:
#     if i < 3:
#         i += 1
#         print(text[k:i])
#         # print(k, i)
#         k += 1
#     else:
#         break

# text = "abcd"
#
# for j in range(len(text)):
#     k = 0
#     i = j
#     while True:
#         if i < len(text):
#             i += 1
#             print(text[k:i])
#             # print(k, i)
#             k += 1
#         else:
#             break


def all_variants(text=""):
    for j in range(len(text)):
        k = 0
        i = j
        while True:
            if i < len(text):
                i += 1
                yield text[k:i]
                # print(k, i)
                k += 1
            else:
                break

a = all_variants("abc")
for i in a:
    print(i)

# b = all_variants("defg")
# for i in b:
#     print(i)
#
# c = all_variants("1234")
# for i in c:
#     print(i)

