class Person:
	def __init__(self, name):
		self._name = name
	def __getattr__(self, attr):
		if attr == 'name':
			print('fetch...')
			return self._name
		else:
			raise AttributeError(attr)

	def __setattr__(self, attr, value):
		if attr == 'name':
			print('change...')
			attr = '_name'
		self.__dict__[attr] = value

	def __delattr__(self, attr):
		if attr == 'name':
			print('remove...')
			attr = '_name'
		del self.__dict__[attr]

bob = Person('Bob Smith') 	# Объект bob обладает управляемым атрибутом
print(bob.name) 			# Вызовет __getattr__
bob.name = 'Robert Smith' 	# Вызовет __setattr__
print(bob.name)
del bob.name 				# Вызовет __delattr__
print('-'*20)
sue = Person('Sue Jones') 	# Объект sue также наследует свойство
print(sue.name)
#print(Person.name.__doc__) # Не имеет эквивалента в данном случае
