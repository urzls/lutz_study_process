for x in ["spam", "eggs", "ham"]:
    print(x, end=' ')
print ('==================')
sum = 0
for x in [1, 2, 3, 4]:
    sum = sum + x
print (sum)
prod = 1
for item in [1, 2, 3, 4]: prod *= item
print (prod)
print ('==================')
S = "lumberjack"
T = ("and", "I’m", "okay")
for x in S:
    print (x, end=' ')
print ('==================')
for x in T:
    print (x, end=' ')
print ('==================')

T = [(1, 2), (3, 4), (5, 6)]
for (a, b) in T:
    print (a, b)
print ('==================')

D = {'a': 1, 'b': 2, 'c': 3}
for key in D:
    print(key, '=>', D[key])

print (list(D.items()))

for (key, value) in D.items():
    print(key, '=>', value)

print ('==================')
for both in T:
    a, b = both
    print (a, b)

