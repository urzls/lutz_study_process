Python 3.7.1 (v3.7.1:260ec2c36a, Oct 20 2018, 14:57:15) [MSC v.1915 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import runme
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import runme
ModuleNotFoundError: No module named 'runme'
>>> 
>>> import runme
>>> 
>>> runme.tester()
It's Christmas in Heaven...
>>> 
>>> import min
I am: min
>>> min.minmax(min.lessthan, ‚s', ‚p', ‚a', ‚m')
SyntaxError: invalid character in identifier
>>> min.minmax(min.lessthan, 's', 'p', 'a', 'm')
'a'
>>> 

sys.path.append('D:\\prog\\Lutz_1') # Дополнение пути поиска модулей
