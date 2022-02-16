Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
====================== RESTART: C:/Python/manynames.py ======================
11
11
22
11
33
55
33
>>> 
====================== RESTART: C:/Python/manynames.py ======================
11
11
22
11
33
55
33
>>> 
====================== RESTART: C:/Python/otherfile.py ======================
66
11
11
22
33
33
55

>>> 
>>> 
>>> 
>>> 
>>> 
>>> class super:
	def hello(self):
		self.data1 = 'spam'

		
>>> class sub(super):
	def hola(self):
		self.data2 = 'eggs'

		
>>> X = sub()
>>> X.__dict__
{}
>>> X.__class__
<class '__main__.sub'>
>>> sub.__bases__
(<class '__main__.super'>,)
>>> super.__bases__
(<class 'object'>,)
>>> 
>>> Y = sub()
>>> X.hello()
>>> X.__dict__
{'data1': 'spam'}
>>> X.hola()
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs'}
>>> sub.__dict__.keys()
dict_keys(['__module__', 'hola', '__doc__'])
>>> super.__dict__.keys()
dict_keys(['__module__', 'hello', '__dict__', '__weakref__', '__doc__'])
>>> Y.__dict__
{}
>>> 
>>> X.data1, X.__dict__['data1']
('spam', 'spam')
>>> X.data3 = 'toast'
>>> X.__dict__
{'data1': 'spam', 'data2': 'eggs', 'data3': 'toast'}
>>> X.__dict__['data3'] = 'ham'
>>> X.data3
'ham'
>>> 
>>> 
>>> X.__dict__, Y.__dict__
({'data1': 'spam', 'data2': 'eggs', 'data3': 'ham'}, {})
>>> list(X.__dict__.keys())
['data1', 'data2', 'data3']
>>> dir(X)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'data1', 'data2', 'data3', 'hello', 'hola']
>>> dir(sub)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'hello', 'hola']
>>> dir(super)
['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'hello']
>>> 
