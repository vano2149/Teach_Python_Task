"""
Операторы присваевания: стр. 363.
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


