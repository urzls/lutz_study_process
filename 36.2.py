Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set(dir('abc')) - set(dir(b'abc'))
{'isnumeric', 'format', 'format_map', 'casefold', 'isidentifier', 'isprintable', 'encode', 'isdecimal'}
>>> set(dir(b'abc')) - set(dir('abc'))
{'fromhex', 'decode', 'hex'}
>>> B = b'spam'
>>> B.find(b'pa')
1
>>> B
b'spam'
>>> 
>>> B[0]
115
>>> B[-1]
109
>>> chr(B[0])
's'
>>> 
>>> 
>>> B = bytes([97, 98, 99,100])
>>> B
b'abcd'
>>> 
>>> 
>>> B
b'abcd'
>>> 
>>> B = b'spam'
>>> B.replace('pa', 'PA')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    B.replace('pa', 'PA')
TypeError: a bytes-like object is required, not 'str'
>>> B.replace(b'pa', b'PA')
b'sPAm'
>>> B = B'spam'
>>> B.replace(bytes('pa'), bytes('xy'))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    B.replace(bytes('pa'), bytes('xy'))
TypeError: string argument without an encoding
>>> 
>>> 
>>> B.replace(bytes('pa', 'ascii'), bytes('xy', 'utf-8'))
b'sxym'
>>> 
>>> b'ab'.decode() + 'cd'
'abcd'
>>> b'ab' + 'cd'.encode()
b'abcd'
>>> b'abcd'
b'abcd'

>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> 
>>> B = b'spam'
>>> C = bytearray(B)
>>> C
bytearray(b'spam')
>>> 
>>> C[0]
115
>>> C[0] = ord{'S')
SyntaxError: invalid syntax
>>> C[0] = ord('S')
>>> C
bytearray(b'Spam')
>>> C[1] = b'X'[0]
>>> C
bytearray(b'SXam')
>>> C[1] = b'Z'[1]
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    C[1] = b'Z'[1]
IndexError: index out of range
>>> 