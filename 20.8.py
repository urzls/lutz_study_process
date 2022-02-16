print ([x * x for x in range(10) if x % 2 == 0])            # Списки упорядочены
print ({x * x for x in range(10) if x % 2 == 0})            # А множества - нет
print ({x: x * x for x in range(10) if x % 2 == 0})         # Как и ключи словаря
print ('=======')
print ([x + y for x in [1, 2, 3] for y in [4, 5, 6]])       # Списки сохраняют дубликаты
print ({x + y for x in [1, 2, 3] for y in [4, 5, 6]})       # А множества - нет
print ({x: y for x in [1, 2, 3] for y in [4, 5, 6]})        # Как и ключи словарей
print ('=======')
print ({x + y for x in 'ab' for y in 'cd'})
print ({x + y: (ord(x), ord(y)) for x in 'zx' for y in 'cv'})
print ({k * 2 for k in ['spam', 'ham', 'sausage', 'hroom'] if k[0] == 'h'})
print ({k.upper(): k * 2 for k in ['spam', 'ham', 'sausage'] if k[0] == 's'})
print ('=======')

