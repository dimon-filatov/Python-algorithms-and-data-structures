# 2). Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random

SIZE = 10
MIN_NUM = 0
MAX_NUM = 50

array = [random.uniform(MIN_NUM, MAX_NUM - 1) for _ in range(SIZE)]
print(array)
print('*' * 50)


def sort(lst):
    def magic(left, right):
        if len(left) == 0:
            return right
        if len(right) == 0:
            return left
        spam = []
        i_left = 0
        i_right = 0
        while len(spam) < len(left) + len(right):
            if left[i_left] < right[i_right]:
                spam.append(left[i_left])
                i_left += 1
            else:
                spam.append(right[i_right])
                i_right += 1
            if i_right == len(right):
                spam += left[i_left:]
            if i_left == len(left):
                spam += right[i_right:]
        return spam

    def make_half(data):
        if len(data) < 2:
            return data
        x = len(data) // 2
        return magic(make_half(data[:x]), make_half(data[x:]))

    return make_half(lst)


print(sort(array))
