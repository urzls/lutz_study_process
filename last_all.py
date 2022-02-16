# Поиск наибольшего файла в единственном каталоге

'''
import os, glob
dirname = r'C:\Python'
allsizes = []
allpy = glob.glob(dirname + os.sep + '*.py')
for filename in allpy:
    filesize = os.path.getsize(filename)
    allsizes.append((filesize, filename))

allsizes.sort()
print(allsizes[:2])
print(allsizes[-2:])

'''


# Поиск наибольшего файла с исходным программным кодом на языке Python
# в дереве каталогов
'''
import sys, os, pprint

if sys.platform[:3] == 'win':
    dirname = r'C:\Python'
else:
    dirname = 'D:\prog\Lutz_1'

allsizes = []
for (thisDir, subsHere, filesHere) in os.walk(dirname):
    for filename in filesHere:
        if filename.endswith('.py'):
            fullname = os.path.join(thisDir, filename)
            fullsize = os.path.getsize(fullname)
            allsizes.append((fullsize, fullname))

allsizes.sort()
pprint.pprint(allsizes[:2])
pprint.pprint(allsizes[-2:])
'''


# Поиск наибольшего файла с исходным программным кодом на языке Python
# в пути поиска модулей
'''
import sys, os, pprint
visited = {}
allsizes = []
for srcdir in sys.path:
    for (thisDir, subsHere, filesHere) in os.walk(srcdir):
        thisDir = os.path.normpath(thisDir) 
        if thisDir.upper() in visited:
            continue
        else:
            visited[thisDir.upper()] = True
        for filename in filesHere:
            if filename.endswith('.py'):
                pypath = os.path.join(thisDir, filename)
                try:
                    pysize = os.path.getsize(pypath)
                except:
                    print('skipping', pypath)
                allsizes.append((pysize, pypath))

allsizes.sort()
pprint.pprint(allsizes[:3])
pprint.pprint(allsizes[-3:])
'''


# Сумма по столбцам, разделенным запятыми, в текстовом файле
'''
filename = 'data.txt'
sums = {}
for line in open(filename):
    cols = line.split(',')
    nums = [int(col) for col in cols]
    for (ix, num) in enumerate(nums):
        sums[ix] = sums.get(ix, 0) + num

for key in sorted(sums):
    print(key, '=', sums[key])
'''


# То же, что и выше, но суммы накапливаются в списке, а не в словаре
'''
import sys
filename = sys.argv[1]
numcols = int(sys.argv[2])
totals = [0] * numcols
for line in open(filename):
    cols = line.split(',')
    nums = [int(x) for x in cols]
    totals = [(x + y) for (x, y) in zip(totals, nums)]

print(totals)
'''


# Регрессивное тестирование результатов работы нескольких сценариев
'''
import os
testscripts = [dict(script='test1.py', args=''),     # Или подставьте свои
               dict(script='test2.py', args='spam')] # значения script/args

for testcase in testscripts:
    commandline = '%(script)s %(args)s' % testcase
    output = os.popen(commandline).read()
    result = testcase['script'] + '.result'
    if not os.path.exists(result):
        open(result, 'w').write(output)
        print('Created:', result)
    else:
        priorresult = open(result).read()
        if output != priorresult:
            print('FAILED:', testcase['script'])
            print(output)
        else:
            print('Passed:', testcase['script'])
'''


# Создание ГИП с помощью tkinter (Tkinter – в Python 2.6): кнопка,
# изменяющая цвет и размер
'''
from tkinter import *
import random
fontsize = 50
colors = ['red', 'green', 'blue', 'yellow', 'orange', 'white', 'cyan', 
          'purple']

def reply(text):
    print(text)
    popup = Toplevel()
    color = random.choice(colors)
    Label(popup, text='Popup', bg='black', fg=color).pack()
    L.config(fg=color)

def timer():
    L.config(fg=random.choice(colors))
    win.after(250, timer)

def grow():
    global fontsize
    fontsize += 5
    L.config(font=('arial', fontsize, 'italic'))
    win.after(100, grow)

win = Tk()
L = Label(win, text='Spam',
          font=('arial', fontsize, 'italic'), fg='yellow', bg='navy', relief=RAISED)

L.pack(side=TOP, expand=YES, fill=BOTH)
Button(win, text='press', command=(lambda: reply('red'))).pack(side=BOTTOM,fill=X)
Button(win, text='timer', command=timer).pack(side=BOTTOM, fill=X)
Button(win, text='grow', command=grow).pack(side=BOTTOM, fill=X)
win.mainloop()
'''


# То же, что и выше, но на основе классов, поэтому каждое окно может
# иметь свою собственную информацию о состоянии
'''

from tkinter import *
import random

class MyGui:
    """
    ГИП с кнопками, которые изменяют цвет и размер надписи
    """
    colors = ['blue', 'green', 'orange', 'red', 'brown', 'yellow']

    def __init__(self, parent, title='popup'):
        parent.title(title)
        self.growing = False
        self.fontsize = 10
        self.lab = Label(parent, text='Gui1', fg='white', bg='navy')
        self.lab.pack(expand=YES, fill=BOTH)
        Button(parent, text='Spam', command=self.reply).pack(side=LEFT)
        Button(parent, text='Grow', command=self.grow).pack(side=LEFT)
        Button(parent, text='Stop', command=self.stop).pack(side=LEFT)

    def reply(self):
        " при нажатии кнопки Spam изменяет цвет случайным образом "
        self.fontsize += 5
        color = random.choice(self.colors)
        self.lab.config(bg=color, font=('courier', self.fontsize, 'bold italic'))

    def grow(self):
        " при нажатии кнопки Grow начинает увеличивать размер надписи "
        self.growing = True
        self.grower()

    def grower(self):
        if self.growing:
            self.fontsize += 5
            self.lab.config(font=('courier', self.fontsize, 'bold'))
            self.lab.after(500, self.grower)

    def stop(self):
        "при нажатии кнопки Stop останавливает увеличение размера"
        self.growing = False

class MySubGui(MyGui):
    colors = ['black', 'purple']

MyGui(Tk(), 'main')
MyGui(Toplevel())
MySubGui(Toplevel())
mainloop()
'''



# Сканирование и обслуживание ящика электронной почты
"""
Проверяет ящик входящей электронной почты, извлекает заголовки писем,
позволяя удалять сообщения не загружая их полностью
"""
'''
import poplib, getpass, sys

mailserver = 'domino.telecom.kz'
mailuser   = 'sanzhar'
mailpasswd = getpass.getpass('SANZHAR' % mailserver)

print('Connecting...')
server = poplib.POP3(mailserver)
server.user(mailuser)
server.pass_(mailpasswd)

try:
    print(server.getwelcome())
    msgCount, mboxSize = server.stat()
    print('There are', msgCount, 'mail messages, size ', mboxSize)
    msginfo = server.list()
    print(msginfo)
    for i in range(msgCount):
        msgnum = i+1
        msgsize = msginfo[1][i].split()[1]
        resp, hdrlines, octets = server.top(msgnum, 0)
        print ('-' * 80)
        print('[%d: octets=%d, size=%s]' % (msgnum, octets, msgsize))
        for line in hdrlines: print(line)

        if input('Print?') in ['y', 'Y']:
            for line in server.retr(msgnum)[1]: print(line)
        if input('Delete?') in ['y', 'Y']:
            print('deleting')
            server.dele(msgnum)
        else:
            print('skipping')

finally:
    server.quit()
raw_input('Bye.')
'''


# CGI-сценарий для взаимодействия с броузером на стороне клиента
#!/usr/bin/python
'''
import cgi
form = cgi.FieldStorage()
print ("Content-type: text/html\n")
print ("<HTML>")
print ("<title>Reply Page</title>")
print ("<BODY>")
if not form.has_key('user'):
    print("<h1>Who are you?</h1>")
else:
    print("<h1>Hello <i>%s</i>!</h1>" % cgi.escape(form['user'].value))
print("</BODY></HTML>")
'''


# Сценарий для заполнения и выполнения запросов к базе данных MySql
'''
from MySQLdb import Connect
conn = Connect(host='localhost', user='root', passwd='darling')
curs = conn.cursor()
try:
    curs.execute('drop database testpeopledb')
except:
    pass

curs.execute('create database testpeopledb')
curs.execute('use testpeopledb')
curs.execute('create table people (name char(30), job char(10), pay int(4))')

curs.execute('insert people values (%s, %s, %s)', ('Bob', 'dev', 50000))
curs.execute('insert people values (%s, %s, %s)', ('Sue', 'dev', 60000))
curs.execute('insert people values (%s, %s, %s)', ('Ann', 'mgr', 40000))

curs.execute('select * from people')
for row in curs.fetchall():
    print(row)

curs.execute('select * from people where name = %s', ('Bob',))
print (curs.description)
colnames = [desc[0] for desc in curs.description]
while True:
    print('-' * 30)
    row = curs.fetchone()
    if not row: break
    for (name, value) in zip(colnames, row):
        print('%s => %s' % (name, value))

conn.commit()
'''


# Сценарий для заполнения базы данных shelve объектами Python
# Дополнительные примеры использования модуля shelve приводятся в главе 27,
# а примеры использования модуля pickle – в главе 30
'''
rec1 = {'name': {'first': 'Bob', 'last': 'Smith'},
        'job': ['dev', 'mgr'],
        'age': 40.5}

rec2 = {'name': {'first': 'Sue', 'last': 'Jones'},
        'job': ['mgr'],
        'age': 35.0}

import shelve
db = shelve.open('dbfile')
db['bob'] = rec1
db['sue'] = rec2
db.close()
'''



# Сценарий для вывода и изменения базы данных shelve,
# созданной предыдущим сценарием
'''
import shelve
db = shelve.open('dbfile')
for key in db:
    print(key, '=>', db[key])
bob = db['bob']
bob['age'] += 1
db['bob'] = bob
db.close()
'''