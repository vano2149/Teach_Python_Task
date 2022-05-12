"""
"""
def solution(s):
    return ''.join(' ' + c if c.isupper() else c for c in s)
        
b = "hiMyNameIvan"

solution(b)

def solution(s):
    st = ""

    for c in s:
        if c.upper() == c:
            st += " " + c
        else:
            st += c

    return st


from collections import Counter

def count(string):
    #return print({c:string.count(c) for c in string})
    return Counter(string)# Делает тоже самое что и верхняя строчка.

a="pflfhfdf"

count(a)

f = ['2', "4", "3"]

g = []

def find_outlier(integers):
    for i in f:
        i = int()
        if i % 2 == 0:
            g.append(i)
    return print(g)

find_outlier(f)