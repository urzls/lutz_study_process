x = 'spam'
while x:
    print(x, end=' ')
    x = x[1:]
print ('\n==================')
a=0; b=10
while a < b:
    print(a, end=' ')
    a += 1
print ('==================')
x = 10
while x:
    x = x-1
    if x % 2 == 0: # Четное? - вывести
        print(x, end=' ')
print ('==================')

while 1:
    name = input('Enter name:')
    if name == 'stop': break
    age = input('Enter age: ')
    print('Hello', name, '=>', int(age) ** 2)

print ('==================')
