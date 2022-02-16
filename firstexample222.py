class Person:
	def __init__(self, name):
		self._name = name

	class Name:
		"name descriptor docs"
		def __get__(self, instance, owner):
			print('fetch...')
			return instance._name
		def __set__(self, instance, value):
			print('change...')
			instance._name = value
		def __delete__(self, instance):
			print('remove...')
			del instance._name
		name = Name()

bob = Person('Bob Smith')   # Объект bob имеет управляемый атрибут
print(bob.name)             # Вызовет Name.__get__
bob.name = 'Robert Smith'   # Вызовет Name.__set__
print(bob.name)
del bob.name                # Вызовет Name.__delete__
print('-'*20)
sue = Person('Sue Jones')   # Объект sue также наследует дескриптор
print(sue.name)
print(Person.Name.__doc__)  # Или: help(Name)

