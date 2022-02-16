class Person:
	def __init__(self, name):
		self._name = name
	def getName(self):
		print('fetch...')
		return self._name
	def setName(self, value):
		print('change...')
		self._name = value
	def delName(self):
		print('remove...')
		del self._name
	name = property(getName, setName, delName, "name property docs")



bob = Person('Bob Smith') 		# Объект bob имеет управляемый атрибут
print(bob.name) 				# Вызовет getName
bob.name = 'Robert Smith' 		# Вызовет setName
print(bob.name)
del bob.name 					# Вызовет delName
print('-'*20)
sue = Person('Sue Jones') 		# Объект sue также наследует свойство
print(sue.name)
print(Person.name.__doc__) 		# Или help(Person.name)

