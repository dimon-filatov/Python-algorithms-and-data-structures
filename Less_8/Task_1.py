# 1) Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.

import hashlib
import hmac

some_str = input('Введи слово на латинице >>> ')
result = set()

for i in range(len(some_str)):
    for j in range(len(some_str), i, -1):
        piece_str = some_str[i:j]
        if len(piece_str) == len(some_str) or len(piece_str) == 0:
            pass
        else:
            my_hash = hmac.new(key=b'password', msg=piece_str.encode('utf-8'), digestmod=hashlib.md5).hexdigest()
            result.add(my_hash)
print(f'В слове {some_str} находится {len(result)} подстрок')
