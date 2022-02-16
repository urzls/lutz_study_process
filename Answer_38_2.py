traceMe = False
def trace(*args):
	if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def accessControl(failIf):
	def onDecorator(aClass):
		if not __debug__:
			return aClass
		else:
			class onInstance:
				def __init__(self, *args, **kargs):
					self.__wrapped = aClass(*args, **kargs)
				def __getattr__(self, attr):
					trace('get:', attr)
					if failIf(attr):
						raise TypeError('private attribute fetch: ' + attr)
					else:
						return getattr(self.__wrapped, attr)
				def __setattr__(self, attr, value):
					trace('set:', attr, value)
					if attr == '_onInstance__wrapped':
						self.__dict__[attr] = value
					elif failIf(attr):
						raise TypeError('private attribute change: ' + attr)
					else:
						setattr(self.__wrapped, attr, value)
			return onInstance
	return onDecorator

def Private(*attributes):
	return accessControl(failIf=(lambda attr: attr in attributes))
def Public(*attributes):
	return accessControl(failIf=(lambda attr: attr not in attributes))

@Private('age')
class Person:
	def __init__(self, name, age):
		self.name = name

self.age = age
X = Person('Bob', 40)
print(X.name)
X.name = 'Sue'
print(X.name)

@Public('name')
class Person:
	def __init__(self, name, age):
		self.name = name
		self.age = age

X = Person('bob', 40) # X – это onInstance
print(X.name) # onInstance встраивает Person
X.name = 'Sue'
print(X.name)
#print(X.age) # ОШИБКА, если сценарий не был запущен как “python -O”
#X.age = 999 # то же самое
#print(X.age) # то же самое

