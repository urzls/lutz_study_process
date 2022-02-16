# Фабрика декораторов классов: применяет любой декоратор ко всем методам класса

from types import FunctionType
from mytools_39 import tracer, timer

def decorateAll(decorator):
	def DecoDecorate(aClass):
		for attr, attrval in aClass.__dict__.items():
			if type(attrval) is FunctionType:
				setattr(aClass, attr, decorator(attrval))
		return aClass
	return DecoDecorate

@decorateAll(tracer)
class Person:
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

