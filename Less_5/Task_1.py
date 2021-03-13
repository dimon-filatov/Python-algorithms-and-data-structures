# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.


from collections import namedtuple

Company = namedtuple('Company', 'name, quarter_1, quarter_2, quarter_3, quarter_4, profit')
all_company = {}
avg_profit = 0
count = int(input('Введи количество предприятий:   '))

for i in range(count):
    name = input('Введи название предприятия:   ')
    q_1 = int(input('Введи прибыль за первый квартал:   '))
    q_2 = int(input('Введи прибыль за второй квартал:   '))
    q_3 = int(input('Введи прибыль за третий квартал:   '))
    q_4 = int(input('Введи прибыль за четвертый квартал:   '))
    profit = q_1 + q_2 + q_3 + q_4
    avg_profit += profit
    all_company[i + 1] = Company(name, q_1, q_2, q_3, q_4, profit)

avg_profit /= len(all_company)

low_profit = []

print(f'Средняя годовая прибыл равна {avg_profit}\n')

print('Компании с годовой прибылью выше среднего:')
for n, comp in all_company.items():
    if comp.profit > avg_profit:
        print(f'{comp.name} имеет годовую прибыль {comp.profit}')
    else:
        low_profit.append(n)
print()
print('*' * 50 + '\n')

print('Компании с годовой прибылью ниже среднего:')
for n in low_profit:
    print(f'{all_company[n].name} имеет годовую прибыль {all_company[n].profit}')
