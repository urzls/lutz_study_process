Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	@staticmethod
	def printNumInstances():
		print("Number of instances created: ", Spam.numInstances)
	a = Spam()
	b = Spam()
	c = Spam()Spam.printNumInstances()
	
SyntaxError: invalid syntax
>>> class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	@staticmethod
	def printNumInstances():
		print("Number of instances created: ", Spam.numInstances)
	a = Spam()
	b = Spam()
	c = Spam()
	Spam.printNumInstances()
	a.printNumInstances()

	
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    class Spam:
  File "<pyshell#13>", line 8, in Spam
    a = Spam()
NameError: name 'Spam' is not defined
>>>  class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	@staticmethod
	def printNumInstances():
		print("Number of instances created: ", Spam.numInstances)
		
SyntaxError: unexpected indent
>>> 
KeyboardInterrupt
>>> 

class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances = Spam.numInstances + 1
	@staticmethod
	def printNumInstances():
		print("Number of instances created: ", Spam.numInstances)

		
>>> a = Spam()
>>> b = Spam()
>>> c = Spam()
>>> Spam.printNumInstances()
Number of instances created:  3
>>> a.printNumInstances()
Number of instances created:  3
>>> 
>>> 
>>> 
>>> class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = funcdef __call__(self, *args):
			
SyntaxError: invalid syntax
>>> class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)
	@tracer
	def spam(a, b, c):
		print a, b, c
		
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(a, b, c)?
>>> class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)
	@tracer
	def spam(a, b, c):
		print (a, b, c)

		
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    class tracer:
  File "<pyshell#38>", line 9, in tracer
    @tracer
NameError: name 'tracer' is not defined
>>> class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)
@tracer
def spam(a, b, c):
	print (a, b, c)

SyntaxError: invalid syntax
>>> class tracer:
	def __init__(self, func):
		self.calls = 0
		self.func = func
	def __call__(self, *args):
		self.calls += 1
		print('call %s to %s' % (self.calls, self.func.__name__))
		self.func(*args)

		
>>> @tracer
def spam(a, b, c):
	print (a, b, c)

	
>>> spam(1, 2, 3)
call 1 to spam
1 2 3
>>> spam('a', 'b', 'c')
call 2 to spam
a b c
>>> spam(4, 5, 6)
call 3 to spam
4 5 6
>>> 
>>> 
>>> class X: pass

>>> class Y: pass

>>> X.a = 1
>>> X.b = 2
>>> X.c = 3
>>> Y.a = X.a + X.b + X.c
>>> for X.i in range(Y.a): print(X.i)

0
1
2
3
4
5
>>> class Record: pass

>>> X = Record()
>>> 
>>> X.name = 'bob'
>>> X.job = 'Pizza maker'
>>> 
>>> 
>>> class C:
	shared = []
	def __init__(self):
		self.perobj = []

		
>>> x = C()
>>> y = C()
>>> y.shared, y.perobj
([], [])
>>> x.shared.append('spam')
>>> x.perobj.append('spam')
>>> x.shared, x.perobj
(['spam'], ['spam'])
>>> y.shared, y.perobj
(['spam'], [])
>>> C.shared
['spam']
>>> 
