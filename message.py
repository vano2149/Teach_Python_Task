"""
Страница 594, Инсрументы функционального програмирования!
"""

'''
L = [lambda x: x ** 2,
    lambda x: x ** 3,
    lambda x: x ** 4]

for f in L:
    print(f(2))

print(L[0](3))
'''
'''
import sys

from tkinter import Button, mainloop

X = Button(
    text = "Press me",
    command = (lambda: sys.stdout.write('Spam\n')),
)

X.pack()
mainloop()'''
'''
def is_valid_IP(strng):
    """
    Проверка валидности IP.
    """
    octets = strng.split('.')
    if len(octets) != 4:
        return False
    for octet in octets:
        if not is_valid_octet(octet):
            return False
        return True

def is_valid_octet(octet):
    if not octet.isdigit():
        return False
    if len(octet) > 1 and octet[0] == '0':
        return False
    octet = int(octet)
    if octet >= 0 and octet <= 255:
        return True
    else:
        return False
    #return print(count == 4)

is_valid_IP('0.0.0.0')
'''
#if i >= '0': Возвращает начало каждого объекта.

import ipaddress

def is_valid_IP(strng):
    try:
        ipaddress.ip_address(strng)
        return True
    except:
        return False



def is_valid_IP(strng):
    return True if len(list(filter(lambda x: x >= 0 and x <= 255  ,[int(i) for i in strng.split(".") if i.isdigit() == True and len(str(int(i))) == len(str(i))]))) == 4 else False