print ('==================')

f = open('9.1.py')
print (next(f))
print (next(f))
print (next(f))
print ('==================')

L = [1, 2, 3]
I = iter(L)
print (I.__next__())
print (I.__next__())
print (I.__next__())
print ('==================')

f = open('9.1.py')
print (iter(f) is f)
print (f.__next__())
print ('==================')

L = [1, 2, 3]
for X in L:
    print(X ** 2, end=' ')
print ('\n==================')
   
I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X ** 2, end=' ')

