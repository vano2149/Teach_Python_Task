"""
"""

def sumtree(L):
    '''
    Сумма вложенных элементов списка
    '''
    tot = 0
    for x in L:
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

L = [1, [2, [3, 4], 5], 6,[7 ,8]]

print(sumtree(L))
print(sumtree([1, [2, [3, [5]]]]))
print(sumtree([[[[[1], 2], 3], 4], 5]))