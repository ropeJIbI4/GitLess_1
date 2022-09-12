#  Реализуйте выдачу случайного числа
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time или datetime (миллисекунды или наносекунды) - для задания случайности
# Учтите, что есть диапазон: от(минимальное) и до (максимальное)


import datetime
import time
print('Введите минимум = ')
min_diap=int(input())
print('Введите максимум = ')
max_diap=int(input())
def random_number(min_diap,max_diap):
    
    rand = int(datetime.datetime.now().strftime('%f')) / 1000000
    rand = int((rand * (max_diap-min_diap))+min_diap)
    if rand>max_diap or rand<min_diap:
        return random_number(min_diap, max_diap)
    else:
        return rand

print(random_number(min_diap,max_diap))