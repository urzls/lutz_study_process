counters = [1, 2, 3, 4, 5]

updated = []
for x in counters:
    updated.append(x + 10)

print (updated)
print ('=========')

def inc(x): return x + 500

print (map(inc, counters))
print ('=========')
print (list(map((lambda x: x + 3), counters)))
print ('=========')

def mymap(func, seq):
    res = []
    for x in seq: res.append(func(x))
    return res

print (list(map(inc, [1, 2, 3, 123456])))
print (mymap(inc, [1, 2, 3]))
print ('=========')

print (pow(3, 4))

