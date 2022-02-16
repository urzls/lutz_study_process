def gensquares(N):
    for i in range(N):
        yield i ** 2

for i in gensquares(5):
    print(i, end = ' : ')
print ('\n=======')

def buildsquares(n):
    res = []
    for i in range(n): res.append(i ** 2)
    return res

for x in buildsquares(5): print(x, end=' : ')
print ('\n=======')

for x in [n ** 2 for n in range(5)]:
    print(x, end=' : ')
print ('\n=======')

for x in map((lambda x:x ** 2), range(5)):
    print(x, end=' : ')
print ('\n=======')

def gen():
    for i in range(10):
        X = yield i
        print(X)

G = gen()
print (next(G))
print (G.send(77))
print (G.send(88))
print (next(G))
