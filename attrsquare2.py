class AttrSquare:
	def __init__(self, start):
		self.value = start

	def __getattribute__(self, attr):
		if attr == 'X':
			return object.__getattribute__(self, 'value') ** 2

	def __setattr__(self, attr, value):
		if attr == 'X':
			attr = 'value'
		object.__setattr__(self, attr, value)

A = AttrSquare(3)
B = AttrSquare(32)
print(A.X)
A.X = 4
print(A.X)
print(B.X)
