Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1
	def printNumInstances(cls):
		print("Number of instances:", cls.numInstances, cls)
	printNumInstances = classmethod(printNumInstances)
class Sub(Spam):
	
SyntaxError: invalid syntax
>>> class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1
	def printNumInstances(cls):
		print("Number of instances:", cls.numInstances, cls)
	printNumInstances = classmethod(printNumInstances)

	
>>> 
>>> 
>>> import test
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    import test
  File "C:\Python\test.py", line 11
    print(“Extra stuff...”, cls)
               ^
SyntaxError: invalid character in identifier
>>> import test
>>> x, y = Sub(), Spam()
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    x, y = Sub(), Spam()
NameError: name 'Sub' is not defined
>>> 
>>> from test import Spam, Sub, Other
>>> x, y = Sub(), Spam()
>>> x.printNumInstances()
Extra stuff... <class 'test.Sub'>
Number of instances: 2 <class 'test.Spam'>
>>> Sub.printNumInstances()
Extra stuff... <class 'test.Sub'>
Number of instances: 2 <class 'test.Spam'>
>>> y.printNumInstances()
Number of instances: 2 <class 'test.Spam'>
>>> 
>>> 
>>> 
>>> z = Other()
>>> z.printNumInstances()
Number of instances: 3 <class 'test.Other'>
>>> 
>>> 
>>> 
>>> 
>>> from test_1 import Spam, Sub, Other
>>> x = Spam()
>>> y1, y2 = Sub(), Sub()
>>> z1, z2, z3 = Other(), Other(), Other()
>>> x.numInstances, y1.numInstances, z1.numInstances
(1, 2, 3)
>>> Spam.numInstances, Sub.numInstances, Other.numInstances
(1, 2, 3)
>>> 
