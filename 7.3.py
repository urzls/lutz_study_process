template = '{0}, {1} and {2}'
print (template.format('spam', 'ham', 'eggs'))

template = '{motto}, {pork} and {food}'
print (template.format(motto='spam', pork='ham', food='eggs'))

template = '{motto}, {0} and {food}'
print (template.format('ham', motto='spam', food='eggs'))

print ('{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2]))

X = '{motto}, {0} and {food}'.format(42, motto=3.14, food=[1, 2])
print (X)

X.split(' and ')
print (X)

Y = X.replace('and', 'but under no circumstances')
print (Y)

import sys
print ('My {1[spam]} runs {0.platform}'.format(sys, {'spam': 'PC'}))
print ('My {config[spam]} runs {sys.platform}'.format(sys=sys, config={'spam': 'PC'}))
print ('================\n')

somelist = list('SPAM')
print (somelist)
print ('first={0[0]}, third={0[2]}'.format(somelist))
print ('first={0}, last={1}'.format(somelist[0], somelist[-1]))

parts = somelist[0], somelist[-1], somelist[1:3]
print ('first={0}, last={1}, middle={2}'.format(*parts))
print ('================\n')

print ('{0:10} = {1:10}'.format('spam', 123.4567))
print ('{0:>10} = {1:>10}'.format('spam', 123.4567))
print ('{0.platform:>10} = {1[item]:>4}'.format(sys, dict(item='PC')))

print ('{0:e}, {1:.3e}, {2:g}'.format(3.14159, 3.14159, 3.14159))
print ('{0:f}, {1:.2f}, {2:07.2f}'.format(3.14159, 3.14159, 3.14159))
print ('================\n')

print ('{0:X}, {1:o}, {2:b}'.format(255, 255, 255))
print (bin(255), int('11111111', 2), 0b11111111)
print (hex(255), int('FF', 16), 0xFF)
print ('================\n')

print ('{0:.2f}'.format(1 / 3.0))
print ('%.2f' % (1 / 3.0))
print ('{0:.{1}f}'.format(1 / 3.0, 8))
print ('%.*f' % (4, 1 / 3.0))
print ('================\n')

print ('{0:.2f}'.format(1.2345))    # Строковый метод
print (format(1.2345, '.2f'))       # Встроенная функция
print ('%.2f' % 1.2345)             # Выражение форматирования
print ('================\n')
























