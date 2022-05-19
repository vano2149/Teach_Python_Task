"""
ГЛАВА 20: страница 626,

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


"""def reverse_words(text):
    res=''
    for i in range(len(text)-1,-1,-1):
        res+=text[i]
    List=[]
    List.append(res.split(" "))

    res = List[0][::-1]
    return res
#Продолжить завтра
n = reverse_words("Привет меня зовут иван!")
print(n)"""



"""
def is_prime(num):
    if num <= 0 or num == 1:
        return False
    elif num % num == 0 and num !=0:
        return True
    else:
        return False
"""
"""
import builtins

class MakeOpen:
    def __init__(self, id):
        self.id = id
        self.original = builtins.open
        builtins.open = self

    def __call__(self, *pargs, **kargs):
        print(f'Custom open call {self.id}', pargs, kargs)
        return self.original(*pargs, **kargs)
"""

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg > res:
            res = arg
        return res


def min2(first, *rest):
    for arg in rest:
        if arg < first:
            first = arg
    return first


def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(3,4,1,2))
print(min2("bb", "aa"))
print(min([2,2], [1,1], [3,3]))
