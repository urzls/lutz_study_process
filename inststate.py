from descstate import *

class InstState:
	def __get__(self, instance, owner):
		print('InstState get')
		return instance._Y * 100
	def __set__(self, instance, value):
		print('InstState set')
		instance._Y = value

class CalcAttrs:
	X = DescState(2)
	Y = InstState()
	def __init__(self):
		self._Y = 3
		self.Z = 4

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z) 	# X и Y - вычисляемые, Z - нет
obj.X = 5 					# Присваивания атрибутам X и Y
							# перехватываются
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

