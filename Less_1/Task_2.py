# Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят, и сколько между ними находится букв.

a = input('Введи букву латинского алфавита:  ').lower()
b = input('Введи люблую другу букву латинского алфавита:  ').lower()

pos_a = ord(a) - ord('a') + 1
pos_b = ord(b) - ord('a') + 1

diff = abs(pos_a - pos_b) - 1

print(f'Позиция первой буквы {pos_a}')
print(f'Позиция второй буквы {pos_b}')
print(f'Мужду буквами {diff} символов')