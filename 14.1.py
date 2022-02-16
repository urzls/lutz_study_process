for x in [1, 2, 3, 4]: print(x ** 2, end=' ')
print ('\n==================')
for x in (1, 2, 3, 4): print(x ** 3, end=' ')
print ('\n==================')
for x in 'spam':       print(x * 2, end=' ')
print ('\n==================')

f = open('9.1.py')
print (f.__next__())
print (f.__next__())
print (f.__next__())
print ('==================')
print ('==================')

for line in open('9.1.py'):
    print (line.upper(), end='')

print ('==================')
print ('==================')

for line in open('9.1.py').readlines():
    print(line.upper(), end='')
    
print ('==================')
print ('==================')

f = open('9.1.py')
while True:
    line = f.readline()
    if not line: break
    print(line.upper(), end='')


print ('==================')

f = open('9.1.py')
print (next(f))
print (next(f))
print (next(f))
print (next(f))
print (next(f))
