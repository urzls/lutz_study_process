def tester(start):
    state = start
    def nested(label):
        print(label, state)
    return nested

F = tester(0)
F('spam')
F('ham')
print ('========================')


def tester(start):
    state = start
    def nested(label):
        nonlocal state
        print(label, state)
        state += 1
    return nested

F = tester(0)
F('spam')
F('ham')
F('cheese')
print ('========================')
G = tester(42)
G('spam')
G('eggs')
G('parrot')
print ('========================')

class tester:
    def __init__(self, start):
        self.state = start
    def nested(self, label):
        print(label, self.state)
        self.state += 1

F = tester(0)
F.nested('spam')
F.nested('ham')
F.nested('gam')
G = tester(42)
G.nested('toast')
G.nested('bacon')
G.nested('eggs')
print ('========================')

class tester:
    def __init__(self, start):
        self.state = start
    def __call__(self, label):
        print(label, self.state)
        self.state += 1

H = tester(99)
H('juice')
H('pancackes')
print ('========================')

def tester(start):
    def nested(label):
        print(label, nested.state)
        nested.state += 1
    nested.state = start
    return nested

F = tester(0)
F('spam')
F('ham')
F('gam')
print (F.state)
    




    
