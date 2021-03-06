import timeit
import cProfile


# Вариант 2. Без помощи Решето Эратосфена.


def var_2(n):
    count = 1
    number = 1
    lst = [2]

    if n == 1:
        return 2

    while count != n:
        number += 2

        for element in lst:
            if number % element == 0:
                break
        else:
            count += 1
            lst.append(number)

    return number


print(timeit.timeit('var_2(10)', number=1000, globals=globals()))  # 0.0142703
print(timeit.timeit('var_2(20)', number=1000, globals=globals()))  # 0.03652220000000002
print(timeit.timeit('var_2(40)', number=1000, globals=globals()))  # 0.11554809999999999
print(timeit.timeit('var_2(80)', number=1000, globals=globals()))  # 0.5651529
print(timeit.timeit('var_2(160)', number=1000, globals=globals()))  # 2.0339912
print(timeit.timeit('var_2(320)', number=1000, globals=globals()))  # 7.8509005
print(timeit.timeit('var_2(640)', number=1000, globals=globals()))  # 31.8071152
print(timeit.timeit('var_2(1280)', number=1000, globals=globals()))  # 129.7836063

cProfile.run('var_2(6_400)')


#       6403 function calls in 5.150 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    5.150    5.150 <string>:1(<module>)
#      1    5.147    5.147    5.149    5.149 Task_2_2.py:8(var_2)
#      1    0.000    0.000    5.150    5.150 {built-in method builtins.exec}
#   6399    0.002    0.000    0.002    0.000 {method 'append' of 'list' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# Вывод по заданию №2
# Task_2_1, алгоритм линейнной сложности, так как при увеличении данных в два раза,
# скорость выполнения алгоритма так же увеличвается в 2.
# При маленьких значениях (до 80) Task_2_2 показывает лучшую скорость выполнения задачи, но при дальнейшим увеличении
# значения, целесообразнее использовать алгоритм Task


# Проверка

def test_func(func):
    test = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for i, item in enumerate(test, start=1):
        assert item == func(i), f'Error {i}'
        print(f'Test {i} OK')

# test_func(var_2)
