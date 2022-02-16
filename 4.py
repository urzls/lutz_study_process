D = {'a': 1, 'b': 2, 'c': 3}
Ks = list(D.keys())
print('===================')
Ks.sort()

for key in Ks: # Обход отсортированного списка ключей
	print(key, '=>', D[key]) # Здесь дважды нажмите клавишу Enter
print('===================')
for key in sorted(D):
	print(key, '=>', D[key])
print('===================')
for c in 'spam':
        print(c.upper())
print('===================')

x = 4
while x > 0:
        print('spam!' * x)
        x -= 1
print('===================')

squares = [x ** 2 for x in [1, 2, 3, 4, 5]]
print(squares)
print('===================')

squares = []
for x in [1, 2, 3, 4, 5]: # Эти же операции выполняет и генератор списков,
        squares.append(x ** 2) # следуя протоколу итераций
print(squares)
print('===================')

if not 'f' in D:
        print('missing')

print('===================')

value = D.get('x', 0) # Попытка получить значение,
print(value) # указав значение по умолчанию

value = D['x'] if 'x' in D else 0 # Выражение if/else
print(value)



























