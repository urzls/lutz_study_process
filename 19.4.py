def func(x, y, z): return x + y + z
print (func(2, 3, 4))

f = lambda x, y, z: x + y + z
print (f(2, 3, 4))

x = (lambda a="fee ", b="fie ", c="foe ": a + b + c)
print (x("wee "))
print ('=========')

def knights():
    title = 'Sir'
    action = (lambda x: title + ' ' + x)
    return action

act = knights()
print (act('Robin'))
print ('=========')

lower = (lambda x, y: x if x < y else y)
print (lower('bb', 'aa'))
print (lower('aa', 'bb'))
print ('=========')

import sys
showall = lambda x: list(map(sys.stdout.write, x))
t = showall(['spam\n', 'toast\n', 'eggs\n'])
print ('=========')

showall = lambda x: [sys.stdout.write(line) for line in x]
t = showall(('bright\n', 'side\n', 'of\n', 'life\n'))
print ('=========')

def action(x):
    return (lambda y: x + y)

act = action(99)
print (act)
print (act(11))
