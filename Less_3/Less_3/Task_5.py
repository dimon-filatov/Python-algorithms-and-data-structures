# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

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


result = 0

stop = index_max_num

if index_min_num < index_max_num:
    start = index_min_num + 1
    step = 1
else:
    start = index_min_num - 1
    step = -1

for j in range(start, stop, step):
    result += array[j]

print(result)
