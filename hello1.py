"""
Поддержка чисел с плавающей запятой: стр. 361.
"""

while True:
    reply = input('Enter text:')
    if reply == 'stop':
        break
    elif not reply.isdigit():
        print('Bad!' * 80)
    else:
        num = int(reply)
        if num < 20:
            print('low!')
        else:
            print(num ** 2)
print('Bye!!!')
