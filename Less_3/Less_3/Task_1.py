# В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

array = [i for i in range(2, 100)]


result = {2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}

for num in array:
    for j in range(2, 10):
        if num % j == 0:
            result[j] += 1

for element, count in result.items():
    print(f'Число {element} встречается {count} раз')
