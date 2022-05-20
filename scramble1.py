'''
Завершите функцию scramble(str1, str2), 
которая возвращает true, если часть символов 
str1 может быть переставлена в соответствии с str2, 
в противном случае возвращает false.

Записи:
Будут использоваться только строчные буквы (a-z). 
Знаки препинания или цифры не будут включены.
Необходимо учитывать производительность.
'''

def scramble(s1, s2):
    ''''''
    Lists1 = []
    Lists2 = []
    for i in s1:
        Lists1.append(i)
    print(s1.count(i))
    for i in s2:
        if i in Lists1:
            Lists2.append(i)
        else:
            return print(False)
    return print(True)
scramble('katas', 'steak')

def scramble(s1,s2):
    for letter in set(s2):
        if s1.count(letter) < s2.count(letter):
            return False
    return True

from collections import Counter
from operator import sub

def scramble(s1,s2):
    return not sub(*map(Counter, (s2,s1)))