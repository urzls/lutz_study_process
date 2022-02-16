import time

class timer:
	def __init__(self, func):
		self.func = func
		self.alltime = 0
	def __call__(self, *args, **kargs):
		start = time.perf_counter()
		result = self.func(*args, **kargs)
		elapsed = time.perf_counter() - start
		self.alltime += elapsed
		print('%s: %.5f, %.5f' % (self.func.__name__, elapsed, self.alltime))
		return result

@timer
def listcomp(N):
	return [x * 2 for x in range(N)]

@timer
def mapcall(N):
	return map((lambda x: x * 2), range(N))

result = listcomp(5) 	# Хронометраж данного вызова, всех вызовов,
listcomp(50000) 		# возвращаемое значение
listcomp(500000)
listcomp(1000000)
print(result)
print('allTime = %s' % listcomp.alltime) 	# Общее время всех вызовов listcomp

print('')
result = mapcall(5)
mapcall(50000)
mapcall(500000)
mapcall(1000000)
print(result)
print('allTime = %s' % mapcall.alltime) 	# Общее время всех вызовов mapcall

print('map/comp = %s' % round(mapcall.alltime / listcomp.alltime, 3))
