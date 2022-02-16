Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> from iters import Squares
>>> for i in Squares(1, 5):
	print(i, end=' ')

	
1 4 9 16 25 
>>> 
>>> X = Squares(1, 5)
>>> I = iter(X)
>>> next(I)
1
>>> next(I)
4
>>> next(I)
9
>>> next(I)
16
>>> next(I)
25
>>> next(I)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    next(I)
  File "C:\Python\iters.py", line 9, in __next__
    raise StopIteration
StopIteration
>>> 
>>> X = Squares(1, 5)
>>> X[1]
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    X[1]
TypeError: 'Squares' object does not support indexing
>>> [n for n in X]
[1, 4, 9, 16, 25]
>>> [n for n in X]
[]
>>> [n for n in Squares(1, 5)]
[1, 4, 9, 16, 25]
>>> list(Squares(1, 3))
[1, 4, 9]
>>> 
>>> def gsquares(start, stop):
	for i in range(start, stop+1):
		yield i ** 2

		
>>> for i in gsquares(1, 5):
	print(i, end=' ')

	
1 4 9 16 25 
>>> [x ** 2 for x in range(1, 6)]
[1, 4, 9, 16, 25]
>>> 
