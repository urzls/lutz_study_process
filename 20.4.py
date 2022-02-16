print ([x ** 2 for x in range(4)])
print ((x ** 2 for x in range(4)))
print (list(x ** 2 for x in range(4)))

G = (x ** 2 for x in range(4))
print (next(G))
print (next(G))
print (next(G))
print (next(G))
print ('=======')
for num in (x ** 2 for x in range(4)):
    print('%s, %s' % (num, num / 2.0))
print ('=======')

print (sum(x ** 2 for x in range(4)))
print (sorted(x ** 2 for x in range(4)))
print (sorted((x ** 2 for x in range(4)), reverse=True))

import math
print (list(map(math.sqrt, (x ** 2 for x in range(4)))))
print ('=======')

G = (c * 4 for c in 'SPAM')
print (list(G))

def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('spam')
print (list(G))
print ('=======')

G = (c * 4 for c in 'SPAM')
print (iter(G) is G)
I1 = iter(G)
print (next(I1))
print (next(I1))
I2 = iter(G)
print (next(I2))
print (list(I1))
I3 = iter(c * 4 for c in 'SPAM')
next(I3)
print ('=======')

def timesfour(S):
    for c in S:
        yield c * 4

G = timesfour('spam')
print (iter(G) is G)
I1, I2 = iter(G), iter(G)
print (next(I1))
print (next(I1))
print (next(I2))
print ('=======')

L = [1, 2, 3, 4]
I1, I2 = iter(L), iter(L)
print (next(I1))
print (next(I1))
print (next(I2))
del L[2:]
print (next(I1))

