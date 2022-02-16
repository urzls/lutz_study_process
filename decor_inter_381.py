Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from tracer import spam
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    from tracer import spam
ModuleNotFoundError: No module named 'tracer'
>>> 
KeyboardInterrupt
>>> 
>>> 
>>> from decorator1 import spam
>>> spam(1, 2, 3)
call 1 to spam
6
>>> spam('a', 'b', 'c')
call 2 to spam
abc
>>> spam.calls
2
>>> spam
<decorator1.tracer object at 0x00000000030C1C50>
>>> 
>>> 
>>> 
>>> from decorator1 import spam, eggs
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    from decorator1 import spam, eggs
ImportError: cannot import name 'eggs' from 'decorator1' (C:\Python\decorator1.py)
>>> from decorator2 import spam, eggs
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    from decorator2 import spam, eggs
  File "C:\Python\decorator2.py", line 7
    print(‘call %s to %s’ % (self.calls, self.func.__name__))
              ^
SyntaxError: invalid character in identifier
>>> 
>>> 
>>> 
>>> from decorator2 import spam, eggs
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    from decorator2 import spam, eggs
  File "C:\Python\decorator2.py", line 7
    print(‘call %s to %s’ % (self.calls, self.func.__name__))
              ^
SyntaxError: invalid character in identifier
>>> from decorator2 import spam, eggs
>>> spam(1, 2, 3)
call 1 to spam
6
>>> spam(a=4, b=5, c=6)
call 2 to spam
15
>>> eggs(2, 16)
call 1 to eggs
65536
>>> eggs(4, y=4)
call 2 to eggs
256
>>> 
====================== RESTART: C:\Python\decorator3.py ======================
call 1 to spam
6
None
call 2 to spam
15
None
methods...
Bob Smith Sue Jones
call 1 to giveRaise
110000.00000000001
call 1 to lastName
call 2 to lastName
Smith Jones
>>> 
====================== RESTART: C:\Python\decorator3.py ======================
call 1 to spam
6
call 2 to spam
15
methods...
Bob Smith Sue Jones
call 1 to giveRaise
110000.00000000001
call 1 to lastName
call 2 to lastName
Smith Jones
>>> 
>>> 
>>> 
>>> 
====================== RESTART: C:\Python\decorator4.py ======================
methods...
Traceback (most recent call last):
  File "C:\Python\decorator4.py", line 33, in <module>
    bob = Person('Bob Smith', 50000)
TypeError: Person() takes no arguments
>>> 
====================== RESTART: C:\Python\decorator4.py ======================
methods...
Bob Smith Sue Jones
call 1 to giveRaise
110000.00000000001
call 1 to lastName
call 2 to lastName
Smith Jones
>>> 
====================== RESTART: C:\Python\decorator4.py ======================
methods...
call 1 to __init__
call 2 to __init__
Bob Smith Sue Jones
110000.00000000001
call 1 to lastName
call 2 to lastName
Smith Jones
>>> 
====================== RESTART: C:\Python\decorator5.py ======================
methods...
call 1 to __init__
call 2 to __init__
Bob Smith Sue Jones
110000.00000000001
call 1 to lastName
call 2 to lastName
Smith Jones
>>> 
====================== RESTART: C:\Python\decorator6.py ======================

Warning (from warnings module):
  File "C:\Python\decorator6.py", line 8
    start = time.clock()
DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead

Warning (from warnings module):
  File "C:\Python\decorator6.py", line 10
    elapsed = time.clock() - start
DeprecationWarning: time.clock has been deprecated in Python 3.3 and will be removed from Python 3.8: use time.perf_counter or time.process_time instead
listcomp: 0.00416, 0.00416
listcomp: 0.00558, 0.00974
listcomp: 0.06761, 0.07735
listcomp: 0.14396, 0.22131
[0, 2, 4, 6, 8]
allTime = 0.22131226799999998

mapcall: 0.00001, 0.00001
mapcall: 0.00001, 0.00002
mapcall: 0.00001, 0.00003
mapcall: 0.00001, 0.00004
<map object at 0x0000000002F6B198>
allTime = 3.7106000000064476e-05
map/comp = 0.0
>>> 
====================== RESTART: C:\Python\decorator6.py ======================
listcomp: 0.00001, 0.00001
listcomp: 0.00594, 0.00595
listcomp: 0.07007, 0.07602
listcomp: 0.13988, 0.21590
[0, 2, 4, 6, 8]
allTime = 0.21589964899999997

mapcall: 0.00001, 0.00001
mapcall: 0.00001, 0.00002
mapcall: 0.00001, 0.00002
mapcall: 0.00001, 0.00003
<map object at 0x0000000002F6B048>
allTime = 2.999999999986347e-05
map/comp = 0.0
>>> 
====================== RESTART: C:\Python\decorator6.py ======================
listcomp: 0.00000, 0.00000
listcomp: 0.01560, 0.01560
listcomp: 0.06240, 0.07800
listcomp: 0.14040, 0.21840
[0, 2, 4, 6, 8]
allTime = 0.2184014

mapcall: 0.00000, 0.00000
mapcall: 0.00000, 0.00000
mapcall: 0.00000, 0.00000
mapcall: 0.00000, 0.00000
<map object at 0x0000000002F6A198>
allTime = 0.0
map/comp = 0.0
>>> 
======================= RESTART: C:\Python\testseqs.py =======================
Traceback (most recent call last):
  File "C:\Python\testseqs.py", line 1, in <module>
    from mytools import timer
  File "C:\Python\mytools.py", line 3
    def timer(label=’’, trace=True):
                     ^
SyntaxError: invalid character in identifier
>>> 
>>> 
>>> 
======================= RESTART: C:\Python\testseqs.py =======================

[CCC]==> listcomp: 0.00001, 0.00001
[CCC]==> listcomp: 0.00600, 0.00601
[CCC]==> listcomp: 0.07047, 0.07648
[CCC]==> listcomp: 0.13659, 0.21307
[0, 2, 4, 6, 8]
allTime = 0.21306623299999994

[MMM]==> mapcall: 0.00001, 0.00001
[MMM]==> mapcall: 0.00001, 0.00002
[MMM]==> mapcall: 0.00001, 0.00003
[MMM]==> mapcall: 0.00001, 0.00004
<map object at 0x0000000002F79BE0>
allTime = 4.223699999994501e-05
map/comp = 0.0
>>> 
>>> 
>>> from mytools import timer
>>> @timer(trace=False)
def listcomp(N):
	return [x * 2 for x in range(N)]

>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> x = listcomp(5000)
>>> listcomp
<mytools.timer.<locals>.Timer object at 0x0000000003023FD0>
>>> listcomp.alltime
0.0016874960000166084
>>> 
>>> 
>>> @timer(trace=True, label='\t=>')
def listcomp(N):
	return [x * 2 for x in range(N)]

>>> x = listcomp(5000)
	=> listcomp: 0.00053, 0.00053
>>> x = listcomp(5000)
	=> listcomp: 0.00052, 0.00105
>>> x = listcomp(5000)
	=> listcomp: 0.00052, 0.00157
>>> listcomp.alltime
0.0015722330000187412
>>> 
