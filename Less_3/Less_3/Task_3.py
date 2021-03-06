# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_num = array[0]
index_max_num = 0
min_num = array[0]
index_min_num = 0

for i, num in enumerate(array):
    if num > max_num:
        max_num = num
        index_max_num = i
    elif num < min_num:
        min_num = num
        index_min_num = i

array[index_max_num] = min_num
array[index_min_num] = max_num

print(array)
