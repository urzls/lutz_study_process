Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> 
>>> import Set
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    import Set
ModuleNotFoundError: No module named 'Set'
>>> 
>>> import setwrapper.py
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    import setwrapper.py
  File "C:\Python\setwrapper.py", line 29
    def __repr__(self): return ‘Set:’ + repr(self.data)
                                  ^
SyntaxError: invalid character in identifier
>>> 
>>> 
>>> import setwrapper
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    import setwrapper
  File "C:\Python\setwrapper.py", line 29
    def __repr__(self): return ‘Set:’ + repr(self.data)
                                  ^
SyntaxError: invalid character in identifier
>>> import setwrapper
>>> 
>>> x = Set([1, 3, 5, 7])
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    x = Set([1, 3, 5, 7])
NameError: name 'Set' is not defined
>>> 
>>> import Set from setwrapper
SyntaxError: invalid syntax
>>> 
>>> 
>>> from setwrapper import Set
>>> 
>>> x = Set([1, 3, 5, 7])
>>> print(x.union(Set([1, 4, 7])))
Set:[1, 3, 5, 7, 4]
>>> print(x | Set([1, 4, 6]))
Set:[1, 3, 5, 7, 4, 6]
>>> Set:[1, 3, 5, 7, 4, 6]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
===================== RESTART: C:\Python\typesubclass.py =====================
['a', 'b', 'c']
['a', 'b', 'c']
(indexing ['a', 'b', 'c'] at 1)
a
(indexing ['a', 'b', 'c'] at 3)
c
['a', 'b', 'c', 'spam']
['spam', 'c', 'b', 'a']
>>> 
>>> 
>>> 
>>> 
===================== RESTART: C:\Python\setsubclass.py =====================
Set:[1, 3, 5, 7] Set:[2, 1, 4, 5, 6] 4
Set:[1, 5] Set:[2, 1, 4, 5, 6, 3, 7]
Set:[1, 5] Set:[1, 3, 5, 7, 2, 4, 6]
Set:[7, 5, 3, 1]

>>> type(I)
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    type(I)
NameError: name 'I' is not defined
>>> 
>>> 
>>> 
>>> class C: pass

>>> I = C()
>>> type(I)
<class '__main__.C'>
>>> I.__class__
<class '__main__.C'>
>>> type(C)
<class 'type'>
>>> C.__class__
<class 'type'>
>>> v
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    v
NameError: name 'v' is not defined
>>> type([1, 2, 3])
<class 'list'>
>>> type(list)
<class 'type'>
>>> list.__class__
<class 'type'>
>>> 
>>> 
>>> 
>>> class C: pass

>>> class D: pass

>>> c = C()
>>> d = D()
>>> type(c) == type(d)
False
>>> type(c), type(d)
(<class '__main__.C'>, <class '__main__.D'>)
>>> c.__class__, d.__class__
(<class '__main__.C'>, <class '__main__.D'>)
>>> c1, c2 = C(), C()
>>> type(c1) == type(c2)
True
>>> 
>>> 
