L = [None] * 20
print(L)
print(type(L))
print(type(type(L)))

print('=========================')


class Worker:
        def __init__(self, name, pay): # Инициализация при создании
                self.name = name # self – это сам объект
                self.pay = pay
        def lastName(self):
                return self.name.split()[-1] # Разбить строку по символам пробела
        def giveRaise(self, percent):
                self.pay *= (1.0 + percent) # Обновить сумму выплат

bob = Worker('Bob Smith', 50000)
sue = Worker('Sue Jones', 60000)

print(bob.lastName())
print(sue.lastName())
sue.giveRaise(.10)
print(sue.pay)
