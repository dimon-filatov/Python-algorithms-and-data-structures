# Записать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число.
# Проанализировать скорость и сложность алгоритмов.
#
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков.
# Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
#
# Второй — без использования «Решета Эратосфена».

import timeit
import cProfile


# Вариант 1. С помощью Решето Эратосфена. Работает при поеске до 6454 натурального числа.


def var_1(n):
    end = 10 * n

    lst = [i for i in range(0, end)]
    lst[1] = 0
    m = 2
    while m < end:
        if lst[m] != 0:
            j = m * 2
            while j < end:
                lst[j] = 0
                j = j + m
        m += 1
    result = []
    for element in lst:
        if element != 0:
            result.append(element)

    return result[n - 1]


print(timeit.timeit('var_1(10)', number=1000, globals=globals()))  # 0.15063869999999996
print(timeit.timeit('var_1(20)', number=1000, globals=globals()))  # 0.27308659999999996
print(timeit.timeit('var_1(40)', number=1000, globals=globals()))  # 0.3974217
print(timeit.timeit('var_1(80)', number=1000, globals=globals()))  # 0.7868054
print(timeit.timeit('var_1(160)', number=1000, globals=globals()))  # 1.6154967000000002
print(timeit.timeit('var_1(320)', number=1000, globals=globals()))  # 3.4839501
print(timeit.timeit('var_1(640)', number=1000, globals=globals()))  # 6.9107506
print(timeit.timeit('var_1(1280)', number=1000, globals=globals()))  # 13.850366999999999

cProfile.run('var_1(6_400)')


#       6418 function calls in 0.099 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.001    0.001    0.099    0.099 <string>:1(<module>)
#      1    0.091    0.091    0.098    0.098 Task_2_1.py:19(var_1)
#      1    0.006    0.006    0.006    0.006 Task_2_1.py:22(<listcomp>)
#      1    0.000    0.000    0.099    0.099 {built-in method builtins.exec}
#   6413    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Проверка

def test_func(func):
    test = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i, item in enumerate(test, start=1):
        assert item == func(i), f'Error {i}'
        print(f'Test {i} OK')

# test_func(var_1)
