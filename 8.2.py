table = {'Python': 'Guido van Rossum',
         'Perl': 'Larry Wall',
         'Tcl': 'John Ousterhout'}

language = 'Python'
creator = table[language]
print (creator)

for lang in table:
    print(lang, '\t', table[lang])

print ('============\n')

Matrix = {}
Matrix[(2, 3, 4)] = 88
Matrix[(7, 8, 9)] = 99

X = 2; Y = 3; Z = 4 # символ ; отделяет инструкции
print (Matrix[(X, Y, Z)])
print (Matrix)
print ('============\n')

if (2,3,6) in Matrix:
    print(Matrix[(2,3,6)])
else:
    print (0)

try:
    print(Matrix[(2,3,6)])
except KeyError:
    print (0)

print (Matrix.get((2,3,4), 0))
print (Matrix.get((2,3,6), 0))
print ('============\n')

rec = {}
rec['name'] = 'mel'
rec['age'] = 45
rec['job'] = 'trainer/writer'

print(rec['name'])
































