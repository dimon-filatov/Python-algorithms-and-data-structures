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

check_array = {}

j = None
max_count = 1
num = None
element = None
count = None

for j in array:
    if j in check_array:
        check_array[j] += 1
    else:
        check_array[j] = 1

for element, count in check_array.items():
    if count > max_count:
        max_count = count
        num = element

if max_count > 1:
    print(f'Число {num} встречается ольше всего ({max_count} раз)')
else:
    print('Все числа встречаются по одному разу')

#

sum_ = 0
el = 0
check_lst = [SIZE, MIN_ITEM, MAX_ITEM, array, check_array, j, max_count, num, element, count]
for i in check_lst:
    sum_i, el_i = show(i)
    sum_ += sum_i
    el += el_i

print(sum_, el)  # 5014 байт и храним 228 элемента

# Самый затратный на память элемент dict (check_array), 1208 байта
