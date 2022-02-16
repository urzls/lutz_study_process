# Этот декоратор может применяться к функциям и к методам
# Вместо класса с методом __call__ используется функция,
# иначе “self” будет представлять экземпляр декоратора!

def tracer(func):
	calls = 0
	def onCall(*args, **kwargs):
		nonlocal calls
		calls += 1
		print('call %s to %s' % (calls, func.__name__))
		return func(*args, **kwargs)
	return onCall

# Может применяться к простым функциям

@tracer
def spam(a, b, c):
	print(a + b + c)

spam(1, 2, 3) # Вызовет onCall(1, 2, 3)
spam(a=4, b=5, c=6)

# Может применяться к методам классов!

class Person:
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
	@tracer
	 # giveRaise = tracer(giverRaise)
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)
	# onCall сохранит ссылку на giveRaise

	@tracer
	def lastName(self):
	# lastName = tracer(lastName)
		return self.name.split()[-1]

print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10) 			# Выховет onCall(sue, .10)
print(sue.pay)
print(bob.lastName(), sue.lastName())

