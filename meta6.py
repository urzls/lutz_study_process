class MetaOne(type):
	def __new__(meta, classname, supers, classdict):
		print('In MetaOne.new:', classname)
		return type.__new__(meta, classname, supers, classdict)

	def toast(self):
		print('toast')

class Super(metaclass=MetaOne):
	def spam(self):
		print('spam')

class C(Super):
	def eggs(self):
		print('eggs')

X = C()
X.eggs()
X.spam()
X.toast()

