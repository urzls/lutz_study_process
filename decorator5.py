class tracer(object):
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args, **kwargs):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		return self.func(*args, **kwargs)
	def __get__(self, instance, owner):
		def wrapper(*args, **kwargs):
			return self(instance, *args, **kwargs)
		return wrapper

@tracer
def spam(a, b, c):
	print(a + b + c)

class Person:
	@tracer
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)

	@tracer
	def lastName(self):
		return self.name.split()[-1]

print('methods...')
bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10) 
print(sue.pay)
print(bob.lastName(), sue.lastName())

