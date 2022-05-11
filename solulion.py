"""
"""
"""
def solution(number):
    l = []
    if number < 0:
        l.append(0)
        return print(l)
    else:
        for i in range(number):
            l.append(i)
        list1 = []
        for k in l:
            if k % 3 == 0 or k % 5 == 0:
                list1.append(k)
        return print(sum(list1))

g = 4
solution(g)   
"""

