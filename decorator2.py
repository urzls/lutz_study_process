class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args, **kwargs):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		return self.func(*args, **kwargs)

@tracer
def spam(a, b, c):
	print(a + b + c)

@tracer
def eggs(x, y):
	print(x ** y)

