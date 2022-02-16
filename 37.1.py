Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
= RESTART: C:\Users\77083\AppData\Local\Programs\Python\Python39\firstexample.py
fetch...
Bob Smith
change...
fetch...
Robert Smith
remove...
--------------------
fetch...
Sue Jones
name property docs
>>> 
>>> 
>>> 
= RESTART: C:\Users\77083\AppData\Local\Programs\Python\Python39\firstexample11.py
fetch...
Bob Smith
change...
fetch...
Robert Smith
remove...
--------------------
fetch...
Sue Jones
name property docs
>>> 
>>> 
>>> 
>>> 
>>> 
====== RESTART: C:\Users\77083\AppData\Local\Programs\Python\Python39\propsquare.py =====
9
16
1024
>>> 
>>> 
>>> 
>>> 
>>> 
======= RESTART: C:\Users\77083\AppData\Local\Programs\Python\Python39\propertyname.py ======
fetch...
Bob Smith
change...
fetch...
Robert Smith
remove...
--------------------
fetch...
Sue Jones
name property docs
>>> 
>>> 
>>> 
>>> 
>>> 
>>>  class Descriptor(object):
	 
SyntaxError: unexpected indent
>>> class Descriptor(object):
	def __get__(self, instance, owner):
		print(self, instance, owner, sep='\n')

		
>>> class Subject:
	attr = Descriptor()

	
>>> X = Subject()
>>> X.attr
<__main__.Descriptor object at 0x000002275EA83F70>
<__main__.Subject object at 0x000002275EA83AF0>
<class '__main__.Subject'>
>>> Subject.attr
<__main__.Descriptor object at 0x000002275EA83F70>
None
<class '__main__.Subject'>
>>> 
>>> 
>>> 
>>> class D:
	def __get__(*args): print('get')

	
>>> class C:
	a = D()

	
>>> X = C()
>>> X.a
get
>>> C.a
get
>>> X.a = 99
>>> X.a
99
>>> list(X._dict__.keys())
Traceback (most recent call last):
  File "<pyshell#40>", line 1, in <module>
    list(X._dict__.keys())
AttributeError: 'C' object has no attribute '_dict__'
>>> list(X.__dict__.keys())
['a']
>>> Y = C()
>>> Y.a
get
>>> C.a
get
>>> 
>>> 
>>> 
>>> 
>>> class D:
	def __get__(*args): print('get')
	def __set__(*args): raise AttributeError('cannot set')

	
>>> class C:
	a = D()

	
>>> X = C()
>>> X.a
get
>>> X.a = 99
Traceback (most recent call last):
  File "<pyshell#58>", line 1, in <module>
    X.a = 99
  File "<pyshell#52>", line 3, in __set__
    def __set__(*args): raise AttributeError('cannot set')
AttributeError: cannot set
>>> 
>>> 
>>> 