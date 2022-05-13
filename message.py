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

import sys

from tkinter import Button, mainloop

X = Button(
    text = "Press me",
    command = (lambda: sys.stdout.write('Spam\n')),
)

X.pack()
mainloop()