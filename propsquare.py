class PropSquare:
    def __init__(self, start):
        self.value = start
    def getX(self):
        return self.value ** 2
    def setX(self, value):
        self.value = value
    X = property(getX, setX)

P = PropSquare(3)       # 2 экземпляра класса со свойством
Q = PropSquare(32)      # Каждый хранит собственное значение
print(P.X)              # 3 ** 2
P.X = 4
print(P.X)              # 4 ** 2
print(Q.X)              # 32 ** 2

