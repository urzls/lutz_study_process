X = 1
import mod2

print (X, end=' ') 			# Моя глобальная переменная X
print (mod2.X, end=' ') 	# Переменная X из модуля mod2
print (mod2.mod3.X)			# Переменная X из модуля mod3