import time
import threading

def write_words(word_count=0, file_name=""):
    with open(file_name, mode='w', encoding="utf-8") as file:
        start_time=time.time()
        for count in range(1,word_count+1):
            file.write(f"Какое-то слово № {count}\n")
            time.sleep(0.1)
        end_time = time.time()
    if file_name=='example4.txt' or file_name=='example8.txt':
        elapsed_time = end_time - start_time
        return print(f'Завершилась запись в файл {file_name}\n'
                     f'Работа потоков:  {elapsed_time}')

    return print(f'Завершилась запись в файл {file_name}')

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

thread1=threading.Thread(target=write_words, args=(10, 'example5.txt'), daemon=True)
thread2=threading.Thread(target=write_words, args=(30, 'example6.txt'), daemon=True)
thread3=threading.Thread(target=write_words, args=(200, 'example7.txt'), daemon=True)
thread4=threading.Thread(target=write_words, args=(100, 'example8.txt'), daemon=True)
thread1.start()
thread1.join()
thread2.start()
thread2.join()
thread3.start()
thread3.join()
thread4.start()
thread4.join()

