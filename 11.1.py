seq = [1, 2, 3, 4]
a, b, c, d = seq
print (a, b, c, d)

a, *b = seq
print (a)
print (b)

a, *b, c = seq
print (a)
print (b)
print (c)
print ('======================')

L = [1, 2, 3, 4]
while L:
    front, *L = L # Получить первый и остальные элементы
    print(front, L) #
    
