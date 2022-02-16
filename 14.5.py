lines = [line.rstrip() for line in open('threenames.py') if line[0] == 'p']
print (lines)
print ('==================')

res = []
for line in open ('threenames.py'):
    if line[0] == 'p':
        res.append (line.rstrip())

print (res)
print ('==================')

print ([x + y for x in 'abc' for y in 'lmn'])
print ('==================')

res = []
for x in 'abc':
    for y in 'lmn':
        res.append(x + y)
print (res)
print ('==================')

for line in open('threenames.py'):
    print(line.upper(), end='')
print ('==================')
print ('==================')

uppers = [line.upper() for line in open('threenames.py')]
print (uppers)
print ('==================')
print (map(str.upper, open('threenames.py')))
print ('==================')
print (list( map(str.upper, open('threenames.py')) ))
print ('==================')
print (sorted(open('threenames.py')))
print ('==================')
print (list(zip(open('threenames.py'), open('threenames.py'))))
print ('==================')
print (list(enumerate(open('threenames.py'))))
print ('==================')
print (list(filter(bool, open('threenames.py'))))
print ('==================')
import functools, operator
print (functools.reduce(operator.add, open('threenames.py')))
print ('==================')
print ('==================')

print (list(open('threenames.py')))
print ('==================')
print (tuple(open('threenames.py')))
print ('==================')
print ('&&'.join(open('threenames.py')))
print ('==================')
a = open('threenames.py')
print (a)
print ('==================')
a, *b = open('threenames.py')
print (a, b)
print ('==================')
print ('==================')
print ('==================')
print (set(open('threenames.py')))
print ('==================')
print ({line for line in open('threenames.py')})
print ('==================')
print ({ix: line for ix, line in enumerate(open('threenames.py'))})
print ('==================')
print ({line for line in open('threenames.py') if line[0] == 'p'})
print ('==================')
print ({ix: line for (ix, line) in enumerate(open('threenames.py')) if line[0]=='p'})
print ('==================')








