if 1:
    print ('true')
else:
    print ('false')

x = 'killer rabbit'
if x == 'roger':
    print ("how's jessica?")
elif x == 'bugs':
    print ("what's up doc?")
else:
    print ('Run away! Run away!')
print ('========================')

choice = 'ham'
print ({'spam': 1.25,
    'ham': 1.99,
    'eggs': 0.99,
    'bacon': 1.10}[choice])
print ('========================')

if choice == 'spam':
    print (1.25)
elif choice == 'ham':
    print (1.99)
elif choice == 'eggs':
    print (0.99)
elif choice == 'bacon':
    print (1.10)
else:
    print ('Bad choice')
print ('========================')

branch = ({'spam': 1.25,
           'ham': 1.99,
           'eggs': 0.99,
           'bacon': 1.10})
print (branch.get('spam', 'Bad choice'))
print (branch.get('facon', 'Bad choice'))
print ('========================')

loice = 'facon'
if loice in branch:
    print(branch[choice])
else:
    print('Bad choice')
