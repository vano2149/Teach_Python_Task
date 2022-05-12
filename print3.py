"""
Эмуляция 
большей части финкционала print()!
"""


import sys

def print3(*args, **kwargs):
    sep = kwargs.get('sep', ' ')
    end = kwargs.get('end', '\n')
    file = kwargs.get('file',sys.stdout)
    output = ''
    first = True
    for arg in args:
        output += ('' if first else sep) + str(arg)
        first = False
    file.write(output + end)

print3(1,2,3)
print3(1,2,3, sep="...")
print(1, [2], (3,), sep="...")
print3(4,5,6, sep='',end='')
print(7,8,9)
