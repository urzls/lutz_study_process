print (list(zip(['a', 'b', 'c'], [1, 2, 3])))
D = dict(zip(['a', 'b', 'c'], [1, 2, 3]))
print (D)

D = {k: v for (k, v) in zip(['a', 'b', 'c'], [1, 2, 3])}
print (D)

D = {x: x ** 2 for x in [1, 2, 3, 4]}
print (D)

D = {c: c * 4 for c in 'SPAM'}
print (D)

D = {c.lower(): c + '!' for c in ['SPAM', 'EGGS', 'HAM']}
print (D)
print ('============')

D = dict.fromkeys(['a', 'b', 'c'], 0)   # Инициализация списком ключей
print (D)

D = {k: 0 for k in ['a', 'b', 'c']}      # То же самое, но с помощью
print (D)                               # генератора словаря

D = dict.fromkeys('spam')               # Из другого итерируемого объекта,
print (D)                               # используются значения по умолчанию

D = {k: None for k in 'spam'}
print (D)
print ('============')

D = dict(a=1, b=2, c=3)
print (D)
K = D.keys()
print (K)
print (list(K))
V = D.values()
print (V)
print (list(V))
print (list(D.items()))

for k in D.keys(): print(k)
for key in D: print(key)
