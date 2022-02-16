Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Callee:
	def __call__(self, *pargs, **kargs):
		print('Called: ', pargs, kargs)

		
>>> C = Callee()
>>> C(1, 2, 3)
Called:  (1, 2, 3) {}
>>> C(1, 2, 3, x=4, y=5)
Called:  (1, 2, 3) {'x': 4, 'y': 5}
>>> 
>>> 
>>> class Prod:
	def __init__(self, value):
		self.value = value
	def __call__(self, other):
		return self.value * other

	
>>> x = Prod(2)
>>> x(3)
6
>>> x(4)
8
>>> class Prod:
	def __init__(self, value):
		self.value = value
	def comp(self, other):
		return self.value * other

	
>>> x = Prod(4)
>>> x.comp(4)
16
>>> x.comp(5)
20
>>> 
