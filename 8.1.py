L = ['abc', 'ABD', 'aBe']
print (sorted(L, key=str.lower, reverse=True))
print (sorted([x.lower() for x in L], reverse=True))
print(L)
print('==============\n')

L = [1, 2]
L.extend ([3,4,5])
print (L)
L.pop()
print (L)
L.reverse ()
print (L)
print (list(reversed(L)))
print('==============\n')

L = ['spam', 'eggs', 'ham']
print (L.index('eggs'))
L.insert(1, 'toast')
print (L)
L.remove('eggs')
print (L)
L.pop(1)
print (L)

