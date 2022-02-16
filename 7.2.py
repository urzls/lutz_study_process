exclamation = 'Ni'
print ("The knights who say %s!" % exclamation)
print ("%d %s %d you %s" % (1, 'spam', 4, 5))
print ("%d -- %s -- %s -- %s" % (42, 3.14159, [1, 2, 3], 56))

x = 1234
res = "integers: ...%d...%-6d...%06d" % (x, x, x)
print(res)
x = 1.23456789
print(x)
print('%e | %f | %g' % (x, x, x))
print('%E' % x)
print('%-6.2f | %05.2f | %+06.1f' % (x, x, x))
print("%s" % x, str(x))
print('%f, %.2f, %.*f, %.15f' % (1/3.0, 1/3.0, 4, 1/3.0, 1/3.0))
print('==================\n')

print ("%(n)d %(x)s" % {"n":1, "x":"spam"})

reply = """
Greetings...
Hello %(name)s!
Your age squared is %(age)s
"""
values = {'name': 'Bob', 'age': 40}
print (reply % values)

food = 'spam'
age = 40
print(vars())

print("%(age)d %(food)s" % vars())
print('==================\n')
print('...начинать со страницы 239...\n')
print('==================\n')





























