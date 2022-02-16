Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> feom adder import *
SyntaxError: invalid syntax
>>> from adder import *
>>> x = Adder()
>>> x.add(1, 2)
not implemented!
>>> x = ListAdder()
>>> x.add([1], [2])
[1, 2]
>>> x = DictAdder()
>>> x.add({1:1}, {2:2})
{1: 1, 2: 2}
>>> x = Adder([1])
>>> x + [2]
not implemented!
>>> x = ListAdder([1])
>>> x + [2]
[1, 2]
>>> [2] + x
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    [2] + x
TypeError: can only concatenate list (not "ListAdder") to list
>>> 
======================== RESTART: C:\Python\adder.py ========================
[1, 2, 3, 4, 5, 6]
>>> 
>>> 
>>> 
>>> class Meta:
	def __getattr__(self, name):
		print('get', name)
	def __setattr__(self, name, value):
		print('set', name, value)

		
>>> x = Meta()
>>> x.append
get append
>>> x.spam = "beef"
set spam beef
>>> x + 2
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    x + 2
TypeError: unsupported operand type(s) for +: 'Meta' and 'int'
>>> x[1]
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    x[1]
TypeError: 'Meta' object does not support indexing
>>> 
>>> 
>>> from setwrapper import Set
>>> x = Set([1, 2, 3, 4])
>>> y = Set([3, 4, 5])
>>> x & y
Set:[3, 4, 5]
>>> x | y
Set:[1, 2, 3, 4, 5]
>>> z = Set("hello")
>>> z[0], z[-1]
('h', 'o')
>>> for c in z: print(c, end='_')

h_e_l_o_
>>> len(z), z
(4, Set:['h', 'e', 'l', 'o'])
>>> z & "mello", z | "mello"
(Set:['m', 'e', 'l', 'o'], Set:['h', 'e', 'l', 'o', 'm'])
>>> 
>>> 
>>> 
>>> from multiset import *
>>> x = MultiSet([1,2,3,4])
>>> y = MultiSet([3,4,5])
>>> z = MultiSet([0,1,2])
>>> 
>>>  x & y, x | y
SyntaxError: unexpected indent
>>> x & y, x | y
(Set:[3, 4], Set:[1, 2, 3, 4, 5])
>>> x.intersect(y, z)
Set:[]
>>> x.union(y, z)
Set:[1, 2, 3, 4, 5, 0]
>>> x.intersect([1,2,3], [2,3,4], [1,2,3])
Set:[2, 3]
>>> x.union(range(10))
Set:[1, 2, 3, 4, 0, 5, 6, 7, 8, 9]
>>> 
>>> 
>>> 
======================== RESTART: C:\Python\lunch.py ========================
burritos
pizza
>>> 
>>> from zoo import Cat, Hacker, Mammal
>>> spot = Cat()
>>> spot.reply()
meow
>>> data = Hacker()
>>> data.reply()
Hello world!
>>> fata = Mammal()
>>> fata.reply()
huh?
>>> 
>>> 
>>> 
>>> 
>>> import parrot
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    import parrot
  File "C:\Python\parrot.py", line 5
    name = ‘customer’
                    ^
SyntaxError: invalid character in identifier
>>> import parrot
>>> parrot.Scene().action()
customer: 'that’s one ex-bird!'
clerk: 'no it isn’t...'
parrot: None
>>> 
>>> 
>>> 
