log = open('log.txt', 'w')
print(1, 2, 3, file=log)
print(4, 5, 6, file=log)
log.close()
print(7, 8, 9)

print(open('log.txt').read())
