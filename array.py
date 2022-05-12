"""
"""
def array(x):
    g = []
    r = []
    for i in x:
        if i % 2 == 0:
            g.append(i)
        r.append(i)
    return print(g, r)

array([1,2,3,4,5,6,7,8,9])