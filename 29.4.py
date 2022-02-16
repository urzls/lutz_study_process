Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======================= RESTART: C:/Python/private.py =======================
Traceback (most recent call last):
  File "C:/Python/private.py", line 22, in <module>
    y.name = 'Sue'
  File "C:/Python/private.py", line 6, in __setattr__
    raise PrivateExc(attrname, self)
PrivateExc: ('name', <__main__.Test2 object at 0x0000000002FF9780>)
>>> 
======================= RESTART: C:/Python/private.py =======================
>>> 
>>> class adder:
	def __init__(self, value=0):
		self.data = value
	def __add__(self, other):
		self.data += other

		
>>> x = adder()
>>> print(x)
<__main__.adder object at 0x0000000002F66748>
>>> x
<__main__.adder object at 0x0000000002F66748>
>>> 
>>> 
>>> class addrepr(adder):
	def __repr__(self):
		return 'addrepr(%s)' % self.data

	
>>> x = addrepr(2)
>>> x + 1
>>> x
addrepr(3)
>>> print(x)
addrepr(3)
>>> str(x), repr(x)
('addrepr(3)', 'addrepr(3)')
>>> 
>>> 
>>> 
>>> class addstr(adder):
	def __str__(self):
		return '[Value: %s]' % self.data

	
>>> x = addstr(3)
>>> x + 1
>>> x
<__main__.addstr object at 0x0000000002FFF5F8>
>>> print(x)
[Value: 4]
>>> str(x), repr(x)
('[Value: 4]', '<__main__.addstr object at 0x0000000002FFF5F8>')
>>> 
>>> 
>>> 
>>> class addboth(adder):
	def __str__(self):
		return '[Value: %s]' % self.data
	def __repr__(self):
		return 'addboth(%s)' % self.data

	
>>> x = addboth(4)
>>> x + 1
>>> x
addboth(5)
>>> print(x)
[Value: 5]
>>> str(x), repr(x)
('[Value: 5]', 'addboth(5)')
>>> 
>>> 
>>> class Printer:
	def __init__(self, val):
		self.val = val
	def __str__(self):
		return str(self.val)

	
>>> objs = [Printer(2), Printer(3)]
>>> for x in objs: print(x)

2
3
>>> print(objs)
[<__main__.Printer object at 0x0000000002FFFEB8>, <__main__.Printer object at 0x0000000002FFF6A0>]
>>> objs
[<__main__.Printer object at 0x0000000002FFFEB8>, <__main__.Printer object at 0x0000000002FFF6A0>]
>>> 
>>> 
>>> class Printer:
	def __init__(self, val):
		self.val = val
	def __repr__(self):
		return str(self.val)

	
>>> objs = [Printer(2), Printer(3)]
>>> for x in objs: print(x)

2
3
>>> print(objs)
[2, 3]
>>> objs
[2, 3]
>>> 
