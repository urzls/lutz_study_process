Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class FirstClass:
	def setdata(self, value):
		self.data = value
	def display(self):
		print(self.data)

		
>>> x = FirstClass()
>>> y = FirstClass()
>>> x.setdata("King Arthur")
>>> y.setdata(3.14159)
>>> x.display()
King Arthur
>>> y.display()
3.14159
>>> x.data = "New value"
>>> x.display()
New value
>>> x.anothername = "spam"
>>> x.display()
New value
>>> 
>>> class SecondClass(FirstClass):
	def display(self):
	    print('Current value = "%s"' % self.data)

	    
>>> z = SecondClass()
>>> z.setdata(42)
>>> z.display()
Current value = "42"
>>> 
>>> 
>>> class ThirdClass(SecondClass):
	def __init__(self, value):
	    self.data = value
	def __add__(self, other):
	    return ThirdClass(self.data + other)
	def __str__(self):
	    return '[ThirdClass: %s]' % self.data
	def mul(self, other):
	    self.data *= other

	    
>>> a = ThirdClass("abc")
>>> a.display()
Current value = "abc"
>>> print(a)
[ThirdClass: abc]
>>> b = a + 'xyz'
>>> b.display()
Current value = "abcxyz"
>>> print(b)
[ThirdClass: abcxyz]
>>> a.mul(3)
>>> print(a)
[ThirdClass: abcabcabc]
>>> 
>>> 


>>> 


>>> 

>>> 


>>> 
