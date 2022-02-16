D = {'a': 1, 'b': 2}
F = open('datafile.pkl', 'wb')
import pickle
pickle.dump(D, F)
F.close()

F = open('datafile.pkl', 'rb')
E = pickle.load(F)
print (E)

print (open('datafile.pkl', 'rb').read())

print ('======================')

F = open('data.bin', 'rb')
data = F.read()
print (data)
