print (list(range(-5, 5)))
filter((lambda x: x > 0), range(-5, 5))

res = []
for x in range(-5, 5):
    if x > 0:
        res.append(x)

print (res)
print ('==========')

from functools import reduce

print (reduce((lambda x, y: x + y), [1, 2, 3, 4]))
print (reduce((lambda x, y: x * y), [1, 2, 3, 4]))
print ('==========')

L = [1, 2, 3, 4]
res = L[0]
for x in L[1:]:
    res = res + x

print (res)
print ('==========')

def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print (myreduce((lambda x, y: x + y), [1, 2, 3, 4, 5]))
print (myreduce((lambda x, y: x * y), [1, 2, 3, 4, 5]))
print ('==========')

import operator, functools

print (functools.reduce(operator.add, [2, 4, 6]))
print (functools.reduce((lambda x, y: x + y), [2, 4, 6]))

print ('==========')
print ('Глава 20! Страница 560...')
print ('==========')
