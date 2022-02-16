def func(a, b, c, d): print(a, b, c, d)

args = (1, 2)
args += (3, 4)
func(*args)
print('========')

args = {'a': 1, 'b': 2, 'c': 3}
args['d'] = 4
func(**args)
print('========')

func(*(1, 2), **{'d': 4, 'c': 3})
func(1, *(2, 3), **{'d': 4})
func(1, c=3, *(2,), **{'d': 4})
func(1, *(2, 3), d=4)
func(1, *(2,), c=3, **{'d':4})
print('========')

def echo(*args, **kwargs): print(args, kwargs)
echo(1, 2, a=3, b=4, v=56)
print('========')

def f(a, *b, c=6, **d): print(a, b, c, d)
f(1, 2, 3, x=4, y=5)
f(1, 2, 3, x=4, y=5, c=7)
f(1, 2, 3, c=7, x=4, y=5)
print('========')

def f(a, c=6, *b, **d): print(a, b, c, d)
f(1, 2, 3, x=4)
print('========')

def f(a, *b, c=6, **d): print(a, b, c, d)
f(1, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), c=7, **dict(x=4, y=5))
f(1, c=7, *(2, 3), **dict(x=4, y=5))
f(1, *(2, 3), **dict(x=4, y=5, c=7))
