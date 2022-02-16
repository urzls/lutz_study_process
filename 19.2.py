def echo(message):
    print(message)

echo('Direct call')
x = echo
x('Indirect call!')

def indirect(func, arg):
    func(arg)

indirect(echo, 'Argument call!')
print ('=========')

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]
for (func, arg) in schedule:
    func(arg)
print ('=========')

def make(label):
    def echo(message):
        print(label + ': ' + message)
    return echo

F = make('Spam')
F('Ham!')
F('Eggs!')
print ('=========')



