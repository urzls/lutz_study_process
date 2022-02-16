'''
def generate():
	return Spam()

class Spam:
	count = 1
	def method(self):
		print(Spam.count)

generate().method()
'''

def generate():
	class Spam:
		count = 1
		def method(self):
			print(self.__class__.count)
	return Spam()

generate().method()

