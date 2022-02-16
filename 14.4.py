L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10
print (L)
print ('==================')

L = [x + 10 for x in L]
print (L)
print ('==================')

res = []
for x in L:
    res.append(x + 10)
print (res)
print ('==================')

f = open('11.1.py')
lines = f.readlines()
print (lines)

lines = [line.rstrip() for line in lines]
print (lines)
print ('==================')

lines = [line.rstrip() for line in open('11.1.py')]
print (lines)
print ('==================')

print ([line.upper() for line in open('threenames.py')])
print ('==================')
print ([line.rstrip().upper() for line in open('threenames.py')])
print ('==================')
print ([line.split() for line in open('threenames.py')])
print ('==================')
print ([line.replace(' ', '!') for line in open('threenames.py')])
print ('==================')
print ([('sys' in line, line[0]) for line in open('threenames.py')])
print ('==================')

lines = [line.rstrip() for line in open('threenames.py') if line[0] == 'p']
print (lines)
