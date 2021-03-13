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

num = array[0]
max_count = 1
count = None
a = None
b = None

for a in range(len(array)):
    count = 1
    for b in range(a + 1, len(array)):
        if array[a] == array[b]:
            count += 1
    if count > max_count:
        max_count = count
        num = array[a]
if max_count > 1:
    print(f'Число {num} встречается ольше всего ({max_count} раз)')
else:
    print('Все числа встречаются по одному разу')

#

sum_ = 0
el = 0
check_lst = [SIZE, MIN_ITEM, MAX_ITEM, array, num, max_count, count, a, b]
for i in check_lst:
    sum_i, el_i = show(i)
    sum_ += sum_i
    el += el_i

print(sum_, el)  # 1960 байт и храним 109 элемента

# Самый затратный на память элемент list (array), 452 байта

# Общиый вывод:
# Самый менее затратный по памяти вариант три (Task_1_3) так как не имеет промежуточных массивов и элементов,
# но с точки срения асимптотики этот выриант самый медленный, так как имеет зависимоть O(n**2).
