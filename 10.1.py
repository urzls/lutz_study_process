'''
while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit( ):
        print ('Bad digit! ' * 4)
    else:
        print (int(reply) ** 2)
print ('Byyyee!')
'''
'''
while True:
    reply = input('Enter text:')
    if reply == 'stop': break
    try:
        num = int(reply)
    except:
        print ('Bad digit! ' * 4)
    else:
        print(int(reply) ** 2)
print ('Byyyee!')
'''
while True:
    reply = input ('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print ('Bad digit! ' * 5)
    else:
        num = int(reply)
        if num < 20:
            print ('Too small digit!')
        else:
            print (num ** 2)
print ('Byyyee!')

print ('Глава 11 !!!')
