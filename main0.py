"""
Вывод четного числа или наоборот.
"""
def numn(x):
    evens = []
    odds = []
    for i in x:
        if i % 2 == 0:
            evens.append(i)
        else:
            odds.append(i)
    if len(evens) == 1:
        return print(evens[0])
    elif len(odds) == 1:
        return print(odds[0])

numn([2,4,6,8,10,11])

            