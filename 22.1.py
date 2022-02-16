# import module111                      # Загрузить модуль целиком
# module111.printer('Hello world!')     # Имя дополняется именем модуля


# from module111 import printer           # Копировать одну переменную
# printer('Hello world!')                 # Имя не требует дополнения


# from module111 import *                   # Скопировать все переменные
# printer('Hello world!')

import simple111
print (simple111.spam)


from small import x, y
x = 42
y[0] = 42


import small
print (small.x)
print (small.y)

