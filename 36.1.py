Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> ord('a')
97
>>> hex(97)
'0x61'
>>> chr(97)
'a'
>>> 
>>> 
>>> B = b'spam'
>>> S = 'eggs'
>>> type(B), type(S)
(<class 'bytes'>, <class 'str'>)
>>> B
b'spam'
>>> S
'eggs'
>>> B[0]< S[0]
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    B[0]< S[0]
TypeError: '<' not supported between instances of 'int' and 'str'
>>> B[0], S[0]
(115, 'e')
>>> list(B), list(S)
([115, 112, 97, 109], ['e', 'g', 'g', 's'])
>>> 
>>> 
>>> B[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    B[0] = 'x'
TypeError: 'bytes' object does not support item assignment
>>> S[0] = 'x'
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    S[0] = 'x'
TypeError: 'str' object does not support item assignment
>>> 
>>> B = B"""
xxx
yyyy
"""
>>> B
b'\nxxx\nyyyy\n'
>>> 
>>> 
>>> 
>>> S = 'eggs'
>>> S.encode
<built-in method encode of str object at 0x0000000003083960>
>>> bytes(S, encoding='ascii')
b'eggs'
>>> B = b'spam'
>>> B.decode()
'spam'
>>> str(B, encoding='ascii')
'spam'
>>> 
>>> 
>>> import sys
>>> sys.platform
'win32'
>>> sys.getdefaultencoding()
'utf-8'
>>> bytes(S)
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    bytes(S)
TypeError: string argument without an encoding
>>> str(B)
"b'spam'"
>>> len(str(B))
7
>>> len(str(B, encoding='ascii'))
4
>>> 
>>> 
>>> 
Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
>>> B = b'\xc4\xe8'
>>> B
b'\xc4\xe8'
>>> len(B)
2
>>> B.decode('latin-1')
'Äè'
>>> B = b'\xc3\x84\xc3\xa8'
>>> B.decode('utf-8')
'Äè'
>>> len(B.decode('utf-8'))
2
>>> 
>>> 
>>> 
>>> 
>>> S= 'A\u00c4B\U000000e8C'
>>> S
'AÄBèC'
>>> eln(S)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    eln(S)
NameError: name 'eln' is not defined
>>> len(S)
5
>>> S.encode('latin-1')
b'A\xc4B\xe8C'
>>> len(S.encode('latin-1'))
5
>>> S.encoce('utf-8')
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    S.encoce('utf-8')
AttributeError: 'str' object has no attribute 'encoce'
>>> S.encode('utf-8')
b'A\xc3\x84B\xc3\xa8C'
>>> len(S.encode('utf-8'))
7
>>> 