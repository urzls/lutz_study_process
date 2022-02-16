Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Super:
	def delegate(self):
		self.action()
	def action(self):
		assert False, 'action must be defined!'

>>> X = Super()
>>> X.delegate()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    X.delegate()
  File "<pyshell#5>", line 3, in delegate
    self.action()
  File "<pyshell#5>", line 5, in action
    assert False, 'action must be defined!'
AssertionError: action must be defined!
>>> delegate
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    delegate
NameError: name 'delegate' is not defined
>>> 
>>> 
>>> X.delegate()
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    X.delegate()
  File "<pyshell#5>", line 3, in delegate
    self.action()
  File "<pyshell#5>", line 5, in action
    assert False, 'action must be defined!'
AssertionError: action must be defined!
>>> 
>>> class Super:
	def delegate(self):
		self.action()
	def action(self):
		raise NotImplementedError(‘action must be defined!’)
	
SyntaxError: invalid character in identifier
>>> class Super:
	def delegate(self):
		self.action()
	def action(self):
		raise NotImplementedError('action must be defined!')

	
>>> X = Super()
>>> X.delegate()
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    X.delegate()
  File "<pyshell#19>", line 3, in delegate
    self.action()
  File "<pyshell#19>", line 5, in action
    raise NotImplementedError('action must be defined!')
NotImplementedError: action must be defined!
>>> class Sub(Super): pass

>>> X = Sub()
>>> X.delegate()
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    X.delegate()
  File "<pyshell#19>", line 3, in delegate
    self.action()
  File "<pyshell#19>", line 5, in action
    raise NotImplementedError('action must be defined!')
NotImplementedError: action must be defined!
>>> class Sub(Super):
	def action(self): print('spam')

	
>>> X = Sub()
>>> X.delegate()
spam
>>> 
