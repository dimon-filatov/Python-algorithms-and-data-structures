import timeit
import cProfile
import random


def make_number(n):
    x = 10 ** (n - 1)
    num = random.randint(1 * x, 9 * x)
    return num


def main(n):
    number = make_number(n)
    even = 0
    odd = 0
    while number > 0:
        if number % 2 == 0:
            even += 1
        else:
            odd += 1
        number = number // 10


print(timeit.timeit('main(10)', number=1000, globals=globals()))  # 0.009358000000000005
print(timeit.timeit('main(20)', number=1000, globals=globals()))  # 0.013975499999999988
print(timeit.timeit('main(40)', number=1000, globals=globals()))  # 0.027989899999999984
print(timeit.timeit('main(80)', number=1000, globals=globals()))  # 0.05183499999999999
print(timeit.timeit('main(160)', number=1000, globals=globals()))  # 0.20692310000000003
print(timeit.timeit('main(320)', number=1000, globals=globals()))  # 0.5789356999999999
print(timeit.timeit('main(640)', number=1000, globals=globals()))  # 2.4011799
print(timeit.timeit('main(1280)', number=1000, globals=globals()))  # 7.714799300000001

cProfile.run('main(100_000)')

#       10 function calls in 44.089 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000   44.089   44.089 <string>:1(<module>)
#      1   44.033   44.033   44.089   44.089 Task_1_3.py:12(main)
#      1    0.055    0.055    0.056    0.056 Task_1_3.py:6(make_number)
#      1    0.000    0.000    0.001    0.001 random.py:200(randrange)
#      1    0.000    0.000    0.001    0.001 random.py:244(randint)
#      1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000   44.089   44.089 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}


# Общий вывод
# При маленьких объемах данных менее время затратный алгоритм является третий,
# но при увеличении обхемов данных 160 знаков, лучше использовать первый алгоритм.
# Второй же алгоритм не рекомендуется исполььзовать, так как он является очень затратным на память,
# а так же не способен работь с большими значениями (свыше 990 знаков).
# Сложность алгоритма Task_1_1    линейная сложность
# Сложность алгоритма Task_1_2    2**n

