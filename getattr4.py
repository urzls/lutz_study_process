class GetAttr:
	eggs = 88
	def __init__(self):
		self.spam = 77
	def __len__(self):
		print('__len__: 42')
		return 42
	def __getattr__(self, attr):
		print('getattr: ' + attr)
		if attr == '__str__':
			return lambda *args: '[Getattr str]'
		else:
			return lambda *args: None

class GetAttribute(object):
	eggs = 88
	def __init__(self):
		self.spam = 77
	def __len__(self):
		print('__len__: 42')
		return 42
	def __getattribute__(self, attr):
		print('getattribute: ' + attr)
		if attr == '__str__':
			return lambda *args: '[GetAttribute str]'
		else:
			return lambda *args: None

for Class in GetAttr, GetAttribute:
	print('\n' + Class.__name__.ljust(50, '='))

	X = Class()
	X.eggs 			# Атрибут класса
	X.spam 			# Атрибут экземпляра
	X.other 		# Отсутствующий атрибут
	len(X) 			# Метод __len__ определен явно

	try:
		X[0]
	except:
		print('fail []')

	try:
		X + 99
	except:
		print('fail +')

	try:
		X()
	except:
		print('fail ()')
	X.__call__()

	print(X.__str__())
	print(X)

