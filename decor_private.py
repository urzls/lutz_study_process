"""
Ограничение на чтение значений частных атрибутов экземпляров классов.
Примеры использования приводятся в программном коде самопроверки, в конце.
Декоратор действует как: Doubler = Private(‘data’, ‘size’)(Doubler).
Функция Private возвращает onDecorator, onDecorator возвращает onInstance,
а в каждый экземпляр onInstance встраивается экземпляр Doubler.
"""

traceMe = False
def trace(*args):
	if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):
	def onDecorator(aClass):
		class onInstance:
			def __init__(self, *args, **kargs):
				self.wrapped = aClass(*args, **kargs)
			def __getattr__(self, attr):
				trace('get:', attr)
				if attr in privates:
					raise TypeError('private attribute fetch: ' + attr)
				else:
					return getattr(self.wrapped, attr)
			def __setattr__(self, attr, value):
				trace('set:', attr, value)
				if attr == 'wrapped':
					self.__dict__[attr] = value
				elif attr in privates:
					raise TypeError('private attribute change: ' + attr)
				else:
					setattr(self.wrapped, attr, value)
		return onInstance
	return onDecorator

if __name__ == '__main__':
	traceMe = True

@Private('data', 'size')
class Doubler:
	def __init__(self, label, start):
		self.label = label
		self.data = start
	def size(self):
		return len(self.data)
	def double(self):
		for i in range(self.size()):
			self.data[i] = self.data[i] * 2
	def display(self):
		print('%s => %s' % (self.label, self.data))

X = Doubler('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])

# Все следующие попытки оканчиваются успехом

print(X.label) 							# Доступ извне класса
X.display(); X.double(); X.display() 	# Перехватывается: проверяется,
										# делегируется
print(Y.label)
Y.display(); Y.double()
Y.label = 'Spam'
Y.display()

# Все следующие попытки терпят неудачу
"""
print(X.size()) # Выведет “TypeError: private attribute fetch: size”
print(X.data)
X.data = [1, 1, 1]
X.size = lambda S: 0
print(Y.data)
print(Y.size())
"""
