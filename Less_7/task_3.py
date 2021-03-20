# 3). Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом. Найдите в массиве медиану.
# Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
#
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).

import random

M = 10
MIN_NUM = 0
MAX_NUM = 100

size = 2 * M + 1
array = [random.randint(MIN_NUM, MAX_NUM - 1) for _ in range(size)]
print(array)
print('*' * 50)

array_2 = array.copy()

while len(array) > 1:

    min_num = array[0]
    i_min = 0
    max_num = array[0]
    i_max = 0

    for i, num in enumerate(array):
        if num <= min_num:
            min_num = num
            i_min = i
        if num >= max_num:
            max_num = num
            i_max = i
    if i_max > i_min:
        array.pop(i_max)
        array.pop(i_min)
    elif i_max < i_min:
        array.pop(i_min)
        array.pop(i_max)
    else:
        array.pop(-1)
        array.pop(0)

print(f'Медиана для списка {array_2} равна {array}')
