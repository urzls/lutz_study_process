class DescState:
	def __init__(self, value):
		self.value = value
	def __get__(self, instance, owner):
		print('DescState get')
		return self.value * 10
	def __set__(self, instance, value):
		print('DescState set')
		self.value = value

class CalcAttrs:
	X = DescState(2)
	Y = 3
	def __init__(self):
		self.Z = 4

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z) 	# X - вычисляется, другие - нет
obj.X = 5 					# Операция присваивания X перехватывается
obj.Y = 6
obj.Z = 7
print(obj.X, obj.Y, obj.Z)

