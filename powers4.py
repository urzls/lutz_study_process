# То же самое, но на основе обобщенного метода __getattribute__ управления
# доступом ко всем атрибутам

class Powers:
	def __init__(self, square, cube):
		self._square = square
		self._cube = cube

	def __getattribute__(self, name):
		if name == 'square':
			return object.__getattribute__(self, '_square') ** 2
		elif name == 'cube':
			return object.__getattribute__(self, '_cube') ** 3
		else:
			return object.__getattribute__(self, name)

	def __setattr__(self, name, value):
		if name == 'square':
			self.__dict__['_square'] = value
		else:
			self.__dict__[name] = value

X = Powers(3, 4)
print(X.square) 	# 3 ** 2 = 9
print(X.cube) 		# 4 ** 3 = 64
X.square = 5
print(X.square) 	# 5 ** 2 = 25

