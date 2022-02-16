#from cardholder_1 import CardHolder
#from cardholder_2 import CardHolder
#from cardholder_3 import CardHolder
from cardholder_4 import CardHolder


bob = CardHolder('1234-5678', 'Bob Smith', 40, '123 main st')
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')
bob.name = 'Bob Q. Smith'
bob.age = 50
bob.acct = '23-45-67-89'
print(bob.acct, bob.name, bob.age, bob.remain, bob.addr, sep=' / ')

sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
print(sue.acct, sue.name, sue.age, sue.remain, sue.addr, sep=' / ')
try:
	sue.age = 200
except:
	print('Bad age for Sue')

try:
	sue.remain = 5
except:
	print("Can’t set sue.remain")

try:
	sue.acct = '1234567'
except:
	print('Bad acct for Sue')


