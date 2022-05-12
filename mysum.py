'''
'''

'''
def mysum(L):
    """
    Демонстрация простейшей рекурсии. 
    """
    print(L)
    if not L:
        return 0
    else:
        return L[0] + mysum(L[1:])

mysum([1,2,3,4,5])
'''
'''
def mysum(L):
    """
    Тернальное выражение!
    """
    return 0 if not L else L[0] + mysum(L[1:])

mysum([1,2,3,4,5])
'''

"""
def mysum(L):
    '''
    Косвенная рекурсия!
    '''
    if not L:
        return nonempty(L)

def nonempty(L):
    '''
    Косвенная рекурсия!
    '''
    return L[0] + mysum(L[1:])

mysum([1.1,2.2,3.3,4.4])
"""

