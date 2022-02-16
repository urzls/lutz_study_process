Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> set(dir(b'abc')) - set(dir(bytearray(b'abc')))
{'__getnewargs__'}
>>> set(dir(bytearray(b'abc'))) - set(dir(b'abc'))
{'__delitem__', 'clear', 'remove', 'copy', 'extend', '__alloc__', '__imul__', '__iadd__', 'insert', '__setitem__', 'reverse', 'pop', 'append'}
>>> 
>>> C
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    C
NameError: name 'C' is not defined
>>> S = 'spam'
>>> C = bytearray(S)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    C = bytearray(S)
TypeError: string argument without an encoding
>>> C = bytearray(S, 'latin1')
>>> C
bytearray(b'spam')
>>> 
>>> C.append(b'LMN')
Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    C.append(b'LMN')
TypeError: an integer is required
>>> C.append(ord('L'))
>>> C
bytearray(b'spamL')
>>> C.extend(b'MNO')
>>> C
bytearray(b'spamLMNO')
>>> C + b'!#'
bytearray(b'spamLMNO!#')
>>> C[-1]
79
>>> C[1:]
bytearray(b'pamLMNO')
>>> C + 4
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    C + 4
TypeError: can't concat int to bytearray
>>> C * 7
bytearray(b'spamLMNOspamLMNOspamLMNOspamLMNOspamLMNOspamLMNOspamLMNO')
>>> B
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    B
NameError: name 'B' is not defined
>>> B = b'spam'
>>> list(B)
[115, 112, 97, 109]
>>> list(C)
[115, 112, 97, 109, 76, 77, 78, 79]
>>> S
'spam'
>>> list(S)
['s', 'p', 'a', 'm']
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
>>> 
>>> 
>>> 
>>> 
>>> file = open('temp', 'w')
>>> size = file.write('abc\n')
>>> file.close()
>>> 
>>> 
>>> file = open('temp')
>>> text = file.read()
>>> text
'abc\n'
>>> print(text)
abc

>>> open('temp', 'w').write('abd\n')
4
>>> open('temp', 'r').read()
'abd\n'
>>> open('temp', 'rb').read()
b'abd\r\n'
>>> open('temp', 'wb').write('abc\n')
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    open('temp', 'wb').write('abc\n')
TypeError: a bytes-like object is required, not 'str'
>>> open(b'temp', 'wb').write('abc\n')
Traceback (most recent call last):
  File "<pyshell#52>", line 1, in <module>
    open(b'temp', 'wb').write('abc\n')
TypeError: a bytes-like object is required, not 'str'
>>> open('temp', 'wb').write(b'abc\n')
4
>>> open('temp', 'r').read()
'abc\n'
>>> open('temp', 'rb').read()
b'abc\n'
>>> 
>>> 
>>> BA = bytearray(b'\x01\x02\x03')
>>> open('temp', 'wb').write(BA)
3
>>> open('temp', 'r').read()
'\x01\x02\x03'
>>> open('temp', 'rb').read()
b'\x01\x02\x03'
>>> 
>>> 
>>> 
>>> 
>>> chr(0xFF)
'ÿ'
>>> chr(0xFE)
'þ'
>>> open('temp', 'wb').write(b'\xFF\xFE\xFD')
3

>>> open('temp', 'rb').read()
b'\xff\xfe\xfd'
>>> open('temp', 'r').read()
'яюэ'
>>> 
