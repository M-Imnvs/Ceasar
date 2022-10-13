import msvcrt
import time
import sys, random

class Steps():
    fix_time = 5 # Укажите время работы таймера 
    def timed_input(caption, timeout = fix_time):
        def echo(c):
            sys.stdout.write(c)
            sys.stdout.flush()        

        echo(caption)
        _input = []
        start = time.monotonic()
        while time.monotonic() - start < timeout: # Если время истекло то функция input завершается
            if msvcrt.kbhit():
                c = msvcrt.getwch()
                if ord(c) == 13:
                    echo('\r\n')
                    break
                _input.append(c)
                echo(c)

        if _input:
            return ''.join(_input)    
    steps = timed_input(f'Введите число сдвигов, в течении {fix_time} секунд\n' ) # Начало таймера
    if steps == None: # Условие, если input в течении указанного вреиени равняетя None, то steps приравнивается рандомное чило
        print('Время ожидания истекло, для продолжения работы программы \nБыло случайным образом использованно число от 0 до 9')
        steps = random.randrange(10)
        print(steps)
    else: # Условие, если input был введен, то steps равняется значению input 
        print('Выбранное количество сдвигов: ', steps)

