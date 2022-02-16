myjob = "hacker"
for c in myjob:
    print(c, end=' ')

print('\n==================\n')

S = 'spam'
print(S[0], S[-2])
print(S[1:3], S[1:], S[:-1])

S = 'abcdefghijklmnop'
print(S[1:10:2])
print(S[::2])

S = 'hello'
print(S[::-1])

S = 'abcedfg'
print(S[5:1:-1])
print(str('spam'), repr('spam'))
print('==================\n')

S = 'spammy'
S = S[:3] + 'xx' + S[5:]
print(S)

S = 'spammy'
S = S.replace('mm', 'xx')
print(S)
print('==================\n')

S = 'xxxxSPAMxxxxSPAMxxxx'
where = S.find('SPAM')
print(where)
S = S[:where] + 'EGGS' + S[(where+4):]
print(S)

S = 'xxxxSPAMxxxxSPAMxxxx'
print(S.replace('SPAM', 'EGGS'))
print(S.replace('SPAM', 'EGGS', 1))
print('==================\n')

S = 'spammy'
L = list(S)
print(L)


L[3] = 'x'
L[4] = 'x'
print(L)

S = ''.join(L)
print(S)

print('SPAM'.join(['eggs', 'sausage', 'ham', 'toast']))
print('==================\n')

line = 'aaa bbb ccc'
cols = line.split()
print(cols)

line = 'bob,hacker,40'
print(line.split(','))

line = "i'mSPAMaSPAMlumberjack"
print(line.split("SPAM"))
print('==================\n')

line = "The knights who say Ni!\n"
print(line.rstrip())
print(line.upper())
print(line.isalpha())
print(line.endswith('Ni!\n'))
print(line.startswith('The'))




















































