# Определить, какое число в массиве встречается чаще всего.

import random

SIZE = 1_000
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

check_array = set(array)
max_count = 1
num = None

for element in check_array:
    count_in_array = array.count(element)
    if count_in_array > max_count:
        max_count = count_in_array
        num = element

if max_count > 1:
    print(f'Число {num} встречается ольше всего ({max_count} раз)')
else:
    print('Все числа встречаются по одному разу')
