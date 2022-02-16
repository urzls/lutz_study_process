def f(a):
    a = 99

b = 88
f(b)
print(b)

def changer(a, b):
    a = 2
    b[1] = 'spam'

X = 5
L = [1, 2]
changer(X, L)
print (X, L)
print ('===========')

def multiple(x, y):
    x = 2
    y = [3, 4]
    return x, y

X = 1
L = [1, 2]
X, L = multiple(X, L)
print (X, L)
