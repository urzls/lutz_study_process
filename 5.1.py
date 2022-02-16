a = 3
b = 4

a + 1, a - 1 # Сложение (3 + 1), вычитание (3 - 1)
b * 3, b / 2 # Умножение (4 * 3), деление (4 / 2)
a % 2, b ** 2 # Деление по модулю (остаток), возведение в степень
2 + 4.0, 2.0 ** b # Смешивание типов, выполняется преобразование

b / 2 + a # То же, что и ((4 / 2) + 3)
print(b / (2.0 + a)) # То же, что и (4 / (2.0 + 3))

print ({x for x in 'spam'})
print ({c * 4 for c in 'spam'})
print ({c * 4 for c in 'spamham'})

S = {c * 4 for c in 'spam'}
print (S | {'mmmm', 'xxxx'})
print(S & {'mmmm', 'xxxx'})

print('===================')

A = ["spam"]
B = A
B[0] = "shrubbery"
print(A)
print(B)

