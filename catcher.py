class Catcher:
	def __getattr__(self, name):
		print('Get:', name)
	def __setattr__(self, name, value):
		print('Set:', name, value)

X = Catcher()
X.job # Выведет “Get: job”
X.pay # Выведет “Get: pay”
X.pay = 99 # Выведет “Set: pay 99”

