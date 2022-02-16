D1 = {'spam':1, 'eggs':3, 'toast':5}
print (D1)
print ('==================')

D1 = {}
D1['spam'] = 1
D1['eggs'] = 3
D1['toast'] = 5


keyz = ['spam', 'eggs', 'toast']
valz = [1, 3, 5]
print (list(zip(keyz, valz)))
print ('==================')

D2 = {}
for (k, v) in zip(keyz, valz): D2[k] = v
print (D2)

keys = ['spam', 'eggs', 'toast']
vals = [1, 3, 5]
D3 = dict(zip(keys, vals))
print (D3)
print ('==================')

S = 'spam'
offset = 0
for item in S:
    print (item, 'appears ot offset', offset)
    offset += 1
print ('==================')

S = 'spam'
for (offset, item) in enumerate(S):
    print (item, 'appears ot offset', offset)
    
print ('==================')
print ('==================')
print ([c * i for (i, c) in enumerate(S)])

print ('Глава 14 !!!!!!')











