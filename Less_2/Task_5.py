# 9. Среди натуральных чисел, которые были введены,
# найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.


num = None
result = None
max_sum = 0

while num != '0':
    sum_num = 0
    num = input('Введи любое натуральное число. Для выхода введи 0:   ')
    for i in num:
        sum_num += int(i)
    if sum_num > max_sum:
        max_sum = sum_num
        result = num

print(f'Число {result} имеет самую большую сумму чисел {max_sum}')
