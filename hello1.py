"""
ГЛАВА 13: стр. 436
"""
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


def func1(): ...
def func(): pass"""


"""
while True:
    name = input('Enter name:')
    if name == 'stop':
        break
    age = input('Enter age:')
    print(f'Hello {name}, {int(age) ** 2}!')
"""


"""
print("-" * 20)
y = int(input("Enter y: "))
print("-" * 20)
x = y // 2
while x > 1:
    if y % x == 0:
        print(y, 'has factor', x)
        print("-" * 20)
        break
    x -=1
else:
    print(y, 'is prime')
    print("-" * 20)
"""


"""
items = ['aaa', 111, (4,5), 2.01]
tests = [(4,5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found!")
"""

dict3 = {}

keys = ['spam', 'eggs', 'toast', 'pizza']
vals = [1,2,3,4]

dict3 = dict(zip(keys, vals))
print(dict3)
