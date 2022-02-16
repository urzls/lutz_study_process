D = {'a':1, 'b':2, 'c':3}
x = iter(D)
print (next(x))
print (next(x))
print (next(x))

for key in D:
    print(key, D[key])
print ('=======')

for line in open('temp.txt'):
    print(line, end='')

print ('=======')
print ('=======')
print ('=======')

print ([x * x for x in range(10)])      # Генератор списков: конструирует список подобно вызову list(generator expr)
print ((x * x for x in range(10)))      # Выражение-генератор: воспроизводит элементы. Скобки часто необязательны
print ({x * x for x in range(10)})      # Генератор множеств, новинка в 3.0 {x, y} – литерал множества в 3.0
print ({x: x * x for x in range(10)})   # Генератор словарей, новинка в 3.0

print ('=======')

print ({x * x for x in range(10)})      # Генератор
print (set(x * x for x in range(10)))   # Генератор и конструктор типа
print ({x: x * x for x in range(10)})
print (dict((x, x * x) for x in range(10)))
print ('=======')

res = set()                             # Эквивалент генератора множеств
for x in range(10):
    res.add(x * x)

print (res)
print ('=======')

res = {}
for x in range(10):
    res[x] = x * x

print (res)
print ('=======')













