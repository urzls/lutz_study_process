a, b, c = (1, 2, 3)
for (a, b, c) in [(1, 2, 3), (4, 5, 6)]:
    print (a, b, c)
print ('==================')
a, *b, c = (1, 2, 3, 4)
print (a, b, c)
for (a, *b, c) in [(1, 2, 3, 4), (5, 6, 7, 8)]:
    print(a, b, c)
print ('==================')

items = ["aaa", 111, (4, 5), 2.01]
tests = [(4, 5), 3.14]
for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")
print ('==================')

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found!")
print ('==================')

seq1 = "spam"
seq2 = "scam"
res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print (res)

print (list(range(5)), list(range(2, 5)), list(range(0, 10, 2)))
