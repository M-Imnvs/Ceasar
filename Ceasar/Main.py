import os.path
from Steps import Steps # Импортируем Функционал шагов шифрования Цезаря 

def Shifr():
    alphabet_ru = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя'  # Руский алфавит 
    alphabet_en = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz' # Английский алфавит
    steps = Steps().steps       # Количество сдвигов, ключ шифровки Цезаря
    symb = '############################################################################################################################'
    shifr = ''  # Итоговый результат
    c = len(alphabet_ru)    # Общий размер алфавита Ru
    d = len(alphabet_en)    # Общиц размер алфавита En 

    fcount = len([f for f in os.listdir('Шифровка/')    # Количество файлов в каталоге "Шифровка"
                if os.path.isfile(os.path.join('Шифровка/', f))])
    filecount = fcount + 1 # +1 к количеству файлов 

    # Открытие файлов №1 для чтения и №2 для сохранения результата 
    with open('test_text.txt', 'r', encoding="UTF-8") as f_reader, open( f'Шифровка/Шифр{filecount}.txt', 'w', encoding="UTF-8") as f_writer:
        f_writer.write(f'file name: test_text.txt\nsteps number: {steps}\n{symb}') # Указать открываемый файл и колличество сдвигов 
        f_writer.write('\n \n')
        for line in f_reader:
            f_writer.writelines(line) # Чтение построчное чтение файла с помощью цикла
            for i in line:
                if i in alphabet_ru:
                    shifr += alphabet_ru[(alphabet_ru.find(i) + steps)%c]  # Процесс шифровки, поиск по буквам и добавление ключа шифрования Ru
                elif i in alphabet_en: 
                    shifr += alphabet_en[(alphabet_en.find(i) + steps)%d]  # Процесс шифровки, поиск по буквам и добавление ключа шифрования En
                else:
                    shifr += i # Если поиск не дал ожидаемых результатов, то неизвестный симвов атоматический запишется в итог 
       
        f_writer.write(f'\n \n{symb}\nfile name: Шифр{filecount}.txt \nsteps number: {steps}')  # Указать в какой файл сохраняет результат
        f_writer.write(f'\n{symb}\n \n{shifr}') # Указать колличество сдигов 

Shifr() 