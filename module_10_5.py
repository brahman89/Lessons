import threading
import time
from multiprocessing import Pool



def read_info(name):
    all_data = []
    with open(name, mode='r', encoding="utf-8") as file:
        for line in file:
            all_data.append(line)


filenames = [f'./file {number}.txt' for number in range(1, 5)]



'''Линейный вызов'''
# start_time = time.time()
# for i in filenames:
#     read_info(i)
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'Завершилась линейное чтение в файлов:время  {elapsed_time}с')

'''Многопроцессный'''

if __name__ == '__main__':
    start_time = time.time()
    with Pool(len(filenames)) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Завершилась чтение в файлов с помощью процессов:время  {elapsed_time}с')

'''Поточный'''
# start_time = time.time()
# for i in filenames:
#     # print(i)
#     thread_i=threading.Thread(target=read_info, args=(i,), daemon=True)
#     thread_i.start()
#     while thread_i.is_alive()==True:
#         thread_i.join()
#         # print('end')
# end_time = time.time()
# elapsed_time = end_time - start_time
# print(f'Завершилась чтение в файлв с помощью потоков: время  {elapsed_time} с')
