Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> obj = Methods()
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    obj = Methods()
NameError: name 'Methods' is not defined
>>> 
>>> class Methods:
	def imeth(self, x):
		print(self, x)
	def smeth(x):
		print(x)
	def cmeth(cls, x):
		print(cls, x)

	
>>> class Methods:
	def imeth(self, x):
		print(self, x)
	def smeth(x):
		print(x)
	def cmeth(cls, x):
		print(cls, x)
	smeth = staticmethod(smeth)
	cmeth = classmethod(cmeth)

	
>>> obj = Methods()
>>> obj.imeth(1)
<__main__.Methods object at 0x0000000002FF5E80> 1
>>> Methods.imeth(obj, 2)
<__main__.Methods object at 0x0000000002FF5E80> 2
>>> Methods.smeth(3)
3
>>> obj.smeth(4)
4
>>> Methods.cmeth(5)
<class '__main__.Methods'> 5
>>> obj.cmeth(6)
<class '__main__.Methods'> 6
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class Spam:
	v

	
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    class Spam:
  File "<pyshell#32>", line 2, in Spam
    v
NameError: name 'v' is not defined

>>> class Spam:
	numInstances = 0
	def __init__(self):
		Spam.numInstances += 1
	def printNumInstances():
		print("Number of instances:", Spam.numInstances)
	printNumInstances = staticmethod(printNumInstances)

	
>>> a = Spam()
>>> b = Spam()
>>> c = Spam()
>>> Spam.printNumInstances()
Number of instances: 3
>>> a.printNumInstances()
Number of instances: 3
>>> 
>>> 
>>> 
>>> class Sub(Spam):
	def printNumInstances():
		print("Extra stuff...")
		Spam.printNumInstances()
	printNumInstances = staticmethod(printNumInstances)

	
>>> a = Sub()
>>> b = Sub()
>>> a.printNumInstances()
Extra stuff...
Number of instances: 5
>>> Sub.printNumInstances()
Extra stuff...
Number of instances: 5
>>> Spam.printNumInstances()
Number of instances: 5
>>> class Other(Spam): pass

>>> c = Other()
>>> c.printNumInstances()
Number of instances: 6
>>> 
