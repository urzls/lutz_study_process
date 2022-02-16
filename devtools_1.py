"""
Файл devtools.py: декоратор функций, выполняющий проверку аргументов на
вхождение в заданный диапазон. Проверяемые аргументы передаются декоратору в
виде именованных аргументов. В фактическом вызове функции аргументы могут
передаваться как в виде позиционных, так и в виде именованных аргументов,
при этом аргументы со значениями по умолчанию могут быть опущены.
Примеры использования приводятся в файле devtools_test.py.
"""

trace = True

def rangetest(**argchecks):
	def onDecorator(func):
		if not __debug__:
			return func
		else:
			import sys
			code = func.__code__
			allargs = code.co_varnames[:code.co_argcount]
			funcname = func.__name__

			def onCall(*pargs, **kargs):
				positionals = list(allargs)
				positionals = positionals[:len(pargs)]

				for (argname, (low, high)) in argchecks.items():
					if argname in kargs:
						if kargs[argname] < low or kargs[argname] > high:
							errmsg = '{0} argument "{1}" not in {2}..{3}'
							errmsg = errmsg.format(funcname, argname,low, high)
							raise TypeError(errmsg)

					elif argname in positionals:
						position = positionals.index(argname)
						if pargs[position] < low or pargs[position] > high:
							errmsg = '{0} argument "{1}" not in {2}..{3}'
							errmsg = errmsg.format(funcname, argname,low, high)
							raise TypeError(errmsg)
					else:
						if trace:
							print('Argument "{0}" defaulted'.format(argname))
				return func(*pargs, **kargs)

			return onCall
	return onDecorator

