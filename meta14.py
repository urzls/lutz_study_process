# Фабрика метаклассов: применяет любой декоратор ко всем методам класса

from types import FunctionType
from mytools_39 import tracer, timer

def decorateAll(decorator):
	class MetaDecorate(type):
		def __new__(meta, classname, supers, classdict):
			for attr, attrval in classdict.items():
				if type(attrval) is FunctionType:
					classdict[attr] = decorator(attrval)
			return type.__new__(meta, classname, supers, classdict)
	return MetaDecorate

class Person(metaclass=decorateAll(timer())):
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
	def giveRaise(self, percent):
		self.pay *= (1.0 + percent)
	def lastName(self):
		return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print(sue.pay)
print(bob.lastName(), sue.lastName())

print('-'*40)
print('%.5f' % Person.__init__.alltime)
print('%.5f' % Person.giveRaise.alltime)
print('%.5f' % Person.lastName.alltime)

