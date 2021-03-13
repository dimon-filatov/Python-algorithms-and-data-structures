# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

# Определить, какое число в массиве встречается чаще всего.

# Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
# Windows 10, 64 bit

import sys
import random


def show(obj):
    byte = 0
    el = 0

    def check(el):
        print(f'{type(el)=}, {sys.getsizeof(el)=}, {el=}')
        return sys.getsizeof(el)

    byte += check(obj)
    el += 1
    if hasattr(obj, '__iter__'):
        if hasattr(obj, 'items'):
            for key, value in obj.items():
                byte += check(key)
                el += 1
                byte += check(value)
                el += 1
        elif not isinstance(obj, str):
            for item in obj:
                byte += check(item)
                el += 1
    return byte, el


#


SIZE = 100
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

check_array = set(array)
max_count = 1
num = None
element = None
count_in_array = None

for element in check_array:
    count_in_array = array.count(element)
    if count_in_array > max_count:
        max_count = count_in_array
        num = element

if max_count > 1:
    print(f'Число {num} встречается ольше всего ({max_count} раз)')
else:
    print('Все числа встречаются по одному разу')

#

sum_ = 0
el = 0
check_lst = [SIZE, MIN_ITEM, MAX_ITEM, array, check_array, max_count, num, element, count_in_array]
for i in check_lst:
    sum_i, el_i = show(i)
    sum_ += sum_i
    el += el_i

print(sum_, el)  # 3986 байт на 172 объекта

# Самый затратный на память элемент set (check_array), 1132 байта
