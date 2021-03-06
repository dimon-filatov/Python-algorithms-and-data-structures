# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

import timeit
import cProfile
import random


# Чтобы при проверке нагрузки не писать огромные числа, напишем отдельную функцию,
# которая гененрирует случайное число из n знаков

def make_number(n):
    x = 10 ** (n - 1)
    num = random.randint(1 * x, 9 * x)
    return num


# Вариант с циклом

def cycle(n):
    num = make_number(n)
    even = 0
    odd = 0
    for i in str(num):
        i = int(i)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


print(timeit.timeit('cycle(10)', number=1000, globals=globals()))  # 0.015057299999999996
print(timeit.timeit('cycle(20)', number=1000, globals=globals()))  # 0.03159730000000002
print(timeit.timeit('cycle(40)', number=1000, globals=globals()))  # 0.042218000000000006
print(timeit.timeit('cycle(80)', number=1000, globals=globals()))  # 0.07079219999999997
print(timeit.timeit('cycle(160)', number=1000, globals=globals()))  # 0.13746770000000003
print(timeit.timeit('cycle(320)', number=1000, globals=globals()))  # 0.2642426
print(timeit.timeit('cycle(640)', number=1000, globals=globals()))  # 0.505521
print(timeit.timeit('cycle(1280)', number=1000, globals=globals()))  # 1.1761020999999998


cProfile.run('cycle(100_000)')

#       11 function calls in 1.564 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    1.564    1.564 <string>:1(<module>)
#      1    0.052    0.052    0.053    0.053 Task_1_1.py:12(make_number)
#      1    1.512    1.512    1.564    1.564 Task_1_1.py:20(cycle)
#      1    0.000    0.000    0.001    0.001 random.py:200(randrange)
#      1    0.000    0.000    0.001    0.001 random.py:244(randint)
#      1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    1.564    1.564 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      2    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
