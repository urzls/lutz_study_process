class Person:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        "name property docs"
        print('fetch...')
        return self._name

    @name.setter
    def name(self, value):
        print('change...')
        self._name = value

    @name.deleter
    def name(self):
        print('remove...')
        del self._name

bob = Person('Bob Smith')   # Объект bob имеет управляемый атрибут
print(bob.name)             # Вызовет метод getter свойства name (name 1)
bob.name = 'Robert Smith'   # Вызовет метод setter свойства name (name 2)
print(bob.name)
del bob.name                # Вызовет метод deleter свойства name (name 3)
print('-'*20)
sue = Person('Sue Jones')   # Объект sue также наследует свойство
print(sue.name)
print(Person.name.__doc__)  # Или: help(Person.name)

