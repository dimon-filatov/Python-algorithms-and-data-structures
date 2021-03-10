# Написать программу сложения и умножения двух положительных целых шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

lst = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
ln = len(lst)
a = deque(input('Введи первое число в шестнадцатеричной системе:   ').upper())
b = deque(input('Введи первое число в шестнадцатеричной системе:   ').upper())

result = deque()
i = '0'
x = None


def check_num(x, len_list):
    if x < len_list:
        def_i = '0'
        return x, def_i
    else:
        x -= len_list
        def_i = '1'
        return x, def_i


while len(a) > 0 and len(b) > 0:
    a_last_character = a.pop()
    b_last_character = b.pop()
    result_char = lst.index(a_last_character) + lst.index(b_last_character) + lst.index(i)
    num, i = check_num(result_char, ln)
    result.appendleft(lst[num])

if len(a) > 0:
    x = a
elif len(b) > 0:
    x = b
if x:
    for _ in range(len(x)):
        x_last_character = x.pop()
        result_char = lst.index(x_last_character) + lst.index(i)
        num, i = check_num(result_char, ln)
        result.appendleft(lst[num])

if i == '1':
    result.appendleft('1')

print(''.join(result))
