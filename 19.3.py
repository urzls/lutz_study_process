def func(a):
    b = 'spam'
    return b * a

print (func(8))
print ('=========')

def func(a: 'spam', b, c: 99):
    return a + b + c

print (func(1, 2, 3))
print (func.__annotations__)
for arg in func.__annotations__:
    print(arg, '=>', func.__annotations__[arg])
print ('=========')

def func(a: 'spam' = 4, b: (1, 10) = 5, c: float = 6) -> int:
    return a + b + c

print (func(1, 2, 3))
print (func())
print (func(1, c=10))
print (func.__annotations__)

