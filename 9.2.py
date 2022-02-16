myfile = open('myfile.txt', 'w')
myfile.write('hello text file\n')
myfile.write('goodbye text file\n')
myfile.write('dassssssssssasdasdasd\n')
myfile.close()

myfile = open('myfile.txt')
myfile.readline()
myfile.readline()
myfile.readline()
myfile.readline()

print (open('myfile.txt').read())


for line in open('myfile.txt'):
    print (line, end='')

print ('======================')
X, Y, Z = 43, 44, 45
S = 'Spam'
D = {'a': 1, 'b': 2}
L = [1, 2, 3]

F = open('datafile.txt', 'w')
F.write(S + '\n')
F.write('%s,%s,%s\n' % (X, Y, Z))
F.write(str(L) + '$' + str(D) + '\n')
F.close()

chars = open('datafile.txt').read()
print (chars)
print ('======================')
F = open('datafile.txt')
line = F.readline()
print (line.rstrip())
line = F.readline()
print (line)
parts = line.split(',')
print (parts)
print (int(parts[1]))
numbers = [int(P) for P in parts]
print (numbers)
print ('======================')

line = F.readline()
print (line)
parts = line.split('$')
print (parts)
print (eval(parts[0]))
objects = [eval(P) for P in parts]
print (objects)
























