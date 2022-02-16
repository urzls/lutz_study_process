def maker(N):
    def action(X):
        return X ** N
    return action

f = maker(2)
print (f)
print (f(3))
print (f(4))
g = maker(3)
print (g(3))
print (f(3))
print ("==========")

def f1():
    x = 88
    f2(x)
def f2(x):
    print(x)
print (f1())
print ("==========")

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i ** x)
    return acts
acts = makeActions()
print (acts[0](2))
print (acts[2](2))
print (acts[4](2))
print ("==========")

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x, i=i: i ** x)
    return acts

acts = makeActions()
print (acts[0](2))
print (acts[2](2))
print (acts[4](2))
print ("==========")

def f1():
    x = 99
    def f2():
        def f3():
            print(x)
        f3()
    f2()
f1()

