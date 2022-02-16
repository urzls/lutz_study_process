Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from number import Number
>>> X = Number(5)
>>> Y = X - 2
>>> Y.data
3
>>> class Indexer:
	def __getitem__(self, index):
		return index ** 2

	
>>> X = Indexer()
>>> X[2]
4
>>> X[5]
25
>>> for i in range(5):
	print(X[i], end='')

	
014916
>>> for i in range(5):
	print(X[i], end=' ')

	
0 1 4 9 16 
>>> 
>>> 
>>> 
>>> L = [5, 6, 7, 8, 9]
>>> L[2:4]
[7, 8]
>>> L[1:]
[6, 7, 8, 9]
>>> L[:-1]
[5, 6, 7, 8]
>>> L[::2]
[5, 7, 9]
>>> 
>>> 
>>> L[slice(2, 4)]
[7, 8]
>>> L[slice(1, None)]
[6, 7, 8, 9]
>>> L[slice(None, -1)]
[5, 6, 7, 8]
>>> L[slice(None, None, 2)]
[5, 7, 9]
>>> 
>>> 
>>> 
>>> 
>>> 
>>> class Indexer:
	data = [5, 6, 7, 8, 9]
	def __getitem__(self, index):
		print('getitem: ', index)
		return self.data[index]

	
>>> X = Indexer()
>>> X[0]
getitem:  0
5
>>> X[1]
getitem:  1
6
>>> X[-1]
getitem:  -1
9
>>> X[2:4]
getitem:  slice(2, 4, None)
[7, 8]
>>> X[1:]
getitem:  slice(1, None, None)
[6, 7, 8, 9]
>>> X[:-1]
getitem:  slice(None, -1, None)
[5, 6, 7, 8]
>>> X[::2]
getitem:  slice(None, None, 2)
[5, 7, 9]
>>> 
>>> 
>>> 
>>> class stepper:
	def __getitem__(self, i):
		return self.data[i]

	
>>> X = stepper()
>>> X.data = "Spam"
>>> 
>>> X[1]
'p'
>>> 
>>> for item in X:
	print(item,ArithmeticError end=' ')
	
SyntaxError: invalid syntax
>>> 
>>> for item in X:
	print(item, end=' ')

	
S p a m 
>>> 
>>> 'p' in X
True
>>> [c for c in X]
['S', 'p', 'a', 'm']
>>> list(map(str.upper, X))
['S', 'P', 'A', 'M']
>>> (a, b, c, d) = X
>>> a,b,c
('S', 'p', 'a')
>>> 
>>> list(X), tuple(X), ''.join(X)
(['S', 'p', 'a', 'm'], ('S', 'p', 'a', 'm'), 'Spam')
>>> X
<__main__.stepper object at 0x000000000321C860>
>>> 
