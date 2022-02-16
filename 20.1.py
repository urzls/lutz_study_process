res = []
for x in 'spam':
    res.append(ord(x))

print(res)

res = list(map(ord, 'spam'))
print(res)

res = [ord(x) for x in 'spam']
print(res)

print ([x ** 2 for x in range(10)])
print (list(map((lambda x: x ** 2), range(10))))
print ('=========')

print ([x for x in range(5) if x % 2 == 0])
print (list(filter((lambda x: x % 2 == 0), range(5))))

res = []
for x in range(5):
    if x % 2 == 0:
        res.append(x)

print (res)

print ([x ** 2 for x in range(10) if x % 2 == 0])
print (list(map((lambda x: x**2), filter((lambda x: x % 2 == 0), range(10)))))
print ('=========')

res = [x + y for x in [7, 100, 2] for y in [100, 200, 300]]
print (res)

res = []
for x in [1000, 100, 2]:
    for y in [100, 200, 300]:
        res.append(x + y)

print (res)
print ('=========')

print ([x + y for x in 'spam' for y in 'SPAM'])

print ([(x, y) for x in range(5) if x % 2 == 0 for y in range(5) if y % 2 == 1])
print ('=========')

res = []
for x in range(5):
    if x % 2 == 0:
        for y in range(5):
            if y % 2 == 1:
                res.append((x, y))

print (res)
