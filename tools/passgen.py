#!/usr/bin/env python3

def alay(data):
    data = data.replace('o', '0')
    data = data.replace('O', '0')
    data = data.replace('i', '1')
    data = data.replace('I', '1')
    data = data.replace('z', '2')
    data = data.replace('Z', '2')
    data = data.replace('e', '3')
    data = data.replace('E', '3')
    data = data.replace('a', '4')
    data = data.replace('A', '4')
    data = data.replace('s', '5')
    data = data.replace('S', '5')
    data = data.replace('G', '6')
    data = data.replace('b', '6')
    data = data.replace('t', '7')
    data = data.replace('T', '7')
    data = data.replace('b', '8')
    data = data.replace('B', '8')
    data = data.replace('g', '9')
    return data

def generate(password):
    open('pass.txt', 'a').write('{}\n'.format(password))
    for a in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(a, password))

    for aa in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(aa, password.upper()))

    for aaa in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(aaa, alay(password)))

    for aaaa in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(aaaa, alay(password.upper())))

    for b in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(password, b))

    for bb in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(password.upper(), bb))

    for bbb in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(alay(password), bbb))

    for bbbb in range(0, 10000):
        open('pass.txt', 'a').write('{}{}\n'.format(alay(password.upper()), bbbb))

    asc = '1234567890'
    no = 5
    for i in range(0, 6):
        open('pass.txt', 'a').write('{}{}\n'.format(asc[:no], password))
        no = no + 1

    no = 5
    for i in range(0, 6):
        open('pass.txt', 'a').write('{}{}\n'.format(password, asc[:no]))
        no = no + 1

    no = 5
    for i in range(0, 6):
        open('pass.txt', 'a').write('{}{}\n'.format(asc[:no], alay(password)))
        no = no + 1

    no = 5
    for i in range(0, 6):
        open('pass.txt', 'a').write('{}{}\n'.format(alay(password), asc[:no]))
        no = no + 1

    desc = '0987654321'
    no = 10
    for i in range(0, 10):
        open('pass.txt', 'a').write('{}{}\n'.format(desc[:no], password))
        no = no - 1

    no = 10
    for i in range(0, 10):
        open('pass.txt', 'a').write('{}{}\n'.format(password, desc[:no]))
        no = no - 1

    no = 10
    for i in range(0, 10):
        open('pass.txt', 'a').write('{}{}\n'.format(desc[:no], alay(password)))
        no = no - 1

    no = 10
    for i in range(0, 10):
        open('pass.txt', 'a').write('{}{}\n'.format(alay(password), desc[:no]))
        no = no - 1

def password_generator():
    while True:
        pasw = input('[?] Password (x = break) : ')
        if pasw == 'x':
        	print('[+] Saved to pass.txt')
        	break
        generate(str(pasw))
