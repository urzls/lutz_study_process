import time

def timer(label='', trace=True):
	def onDecorator(func):
		def onCall(*args, **kargs):
			start = time.perf_counter()
			result = func(*args, **kargs)
			elapsed = time.perf_counter() - start
			onCall.alltime += elapsed
			if trace:
				format = '%s%s: %.5f, %.5f'
				values = (label, func.__name__, elapsed, onCall.alltime)
				print(format % values)
			return result
		onCall.alltime = 0
		return onCall
	return onDecorator

# Проверка на функциях

@timer(trace=True, label='[CCC]==>')
def listcomp(N):
	return [x * 2 for x in range(N)]

@timer(trace=True, label='[MMM]==>')
def mapcall(N):
	return list(map((lambda x: x * 2), range(N)))

for func in (listcomp, mapcall):
	result = func(5)
	func(5000000)
	print(result)
	print('allTime = %s\n' % func.alltime)

class Person:
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay

	@timer()
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)

	@timer(label='**')
	def lastName(self):
		return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
bob.giveRaise(.10)
sue.giveRaise(.20)
print(bob.pay, sue.pay)
print(bob.lastName(), sue.lastName())
print('%.5f %.5f' % (Person.giveRaise.alltime, Person.lastName.alltime))

# Ожидаемые результаты

