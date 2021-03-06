import timeit
import cProfile
import random


def make_number(n):
    x = 10 ** (n - 1)
    num = random.randint(1 * x, 9 * x)
    return num


def if_num_even(x):
    if x % 2 == 0:
        return True
    return False


def revers(num, even=0, odd=0):
    if num == 0:
        return even, odd
    else:
        x = num % 10
        if if_num_even(x):
            even += 1
        else:
            odd += 1
        return revers(num // 10, even, odd)


def main(n):
    num = make_number(n)
    return revers(num)


print(timeit.timeit('main(10)', number=1000, globals=globals()))  # 0.017652100000000004
print(timeit.timeit('main(20)', number=1000, globals=globals()))  # 0.029412999999999995
print(timeit.timeit('main(40)', number=1000, globals=globals()))  # 0.0469729
print(timeit.timeit('main(80)', number=1000, globals=globals()))  # 0.1233174
print(timeit.timeit('main(160)', number=1000, globals=globals()))  # 0.35720399999999997
print(timeit.timeit('main(320)', number=1000, globals=globals()))  # 0.7992276
print(timeit.timeit('main(640)', number=1000, globals=globals()))  # 2.7741477

cProfile.run('main(990)')

#       1991 function calls (1001 primitive calls) in 0.008 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.008    0.008 <string>:1(<module>)
#    990    0.000    0.000    0.000    0.000 Task_1_2.py:12(if_num_even)
#  991/1    0.007    0.000    0.008    0.008 Task_1_2.py:18(revers)
#      1    0.000    0.000    0.008    0.008 Task_1_2.py:30(main)
#      1    0.000    0.000    0.000    0.000 Task_1_2.py:6(make_number)
#      1    0.000    0.000    0.000    0.000 random.py:200(randrange)
#      1    0.000    0.000    0.000    0.000 random.py:244(randint)
#      1    0.000    0.000    0.000    0.000 random.py:250(_randbelow_with_getrandbits)
#      1    0.000    0.000    0.008    0.008 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'bit_length' of 'int' objects}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#      1    0.000    0.000    0.000    0.000 {method 'getrandbits' of '_random.Random' objects}
