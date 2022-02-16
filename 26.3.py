Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class rec: pass

>>> rec.name= 'bob'
>>> rec.age = 40
>>> 
>>> print(rec.name)
bob
>>> x = rec()
>>> y = rec()
>>> x.name, y.name
('bob', 'bob')
>>> x.name = 'sue'
>>> rec.name, x.name, y.name
('bob', 'sue', 'bob')
>>> 
>>> rec.__dict__.keys()
dict_keys(['__module__', '__dict__', '__weakref__', '__doc__', 'name', 'age'])
>>> list(x.__dict__.keys())
['name']
>>> list(y.__dict__.keys())
[]
>>> x.__class__
<class '__main__.rec'>
>>> rec.__bases__
(<class 'object'>,)
>>> 
>>> 
>>> def upperName(self):
	return self.name.upper()

>>> upperName(x)
'SUE'
>>> rec.method = upperName
>>> x.method()
'SUE'
>>> y.method()
'BOB'
>>> rec.method(x)
'SUE'
>>> 
>>> rec = {}
>>> rec['name'] = 'mel'
>>> rec['age'] = 40
>>> rec['job'] = 'trainer'/writer
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    rec['job'] = 'trainer'/writer
NameError: name 'writer' is not defined
>>> rec['job'] = 'trainer/writer'
>>> print (rec['name'])
mel
>>> 
>>> 
>>> class rec: pass

>>> rec.name = 'mel'
>>> rec.age = 40
>>> rec.job = 'trainer/writer'
>>> 
>>> print(rec.age)
40
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class rec: pass

>>> pers1 = rec()
>>> pers1.name = 'mel'
>>> pers1.job = 'tra'
>>> pers1.age = 40
>>> 
>>> pers2 = rec()
>>> pers2.name = 'dava'
>>> pers2.job = 'developer'
>>> 
>>> pers1.name, pers2.name
('mel', 'dava')
>>> pers1.job = 'tra'
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class Person:
	def __init__(self, name, job):
	    self.name = name
	    self.job = job
	def info(self):
	    return (self.name, self.job)

	
>>> rec1 = Person('mel', 'trainer')
>>> rec2 = Person('vls', 'developer')
>>> rec1.job, rec2.info()
('trainer', ('vls', 'developer'))
>>> 
>>> rec1.info, rec2.name()
Traceback (most recent call last):
  File "<pyshell#82>", line 1, in <module>
    rec1.info, rec2.name()
TypeError: 'str' object is not callable
>>> rec1.info(), rec2.name
(('mel', 'trainer'), 'vls')
>>> 
