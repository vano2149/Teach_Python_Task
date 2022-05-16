"""
"""

'''
code = 13
a = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ"
def rot13(message):
    c = ''
    for i in message:
        number = a.find(i)
        new_number = number + code
        print(new_number)
        
        
rot13("ghbdtn")

'''

'''
def rot13(message):
    ''''''
    for i in message:
        print(ord(i))
        l = ord(i) + 13
        if l <= 122:
            print(chr(l))
        else:
            l -= 122
            print(chr(l + 65))
'''


def rot13(message):
    ''''''
    for i in message:
        if i.isupper():
            i.lower()
        if ord(i) < 96 or ord(i) > 122:
            print(i)
        else:
            k = ord(i) + 13
            if k > 97 and k <= 122:
                print(chr(k))
            else:
                print(chr(k - 122 + 96))
#от 97 до 122
rot13("test")


