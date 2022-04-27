"""
ГЛАВА 12: Проверки if и правила синтаксиса: стр. 400.
"""

while True:
    reply = input('Entet text: ')
    if reply == 'stop':
        break
    try:
        print(float(reply) ** 2)
    except:
        print("Bad!" * 8)
print('Bye!')


