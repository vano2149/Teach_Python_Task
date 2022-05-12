"""
Страница 565!
"""

def intersect(*args):
    """
    """
    res = []
    for x in args[0]:
        if x in res:
            continue
        for other in args[1:]:
            if x not in other:
                break
        else:
            res.append(x)
    return print(res)

intersect([1,2,3], (1,4))

def union(*args):
    """
    """
    res =[]
    for seq in args:
        for x in seq:
            if x not in res:
                res.append(x)
    return print(res)

s1 = "SPAM"
s2 = "SCAM"
s3 = "SLAM"
union(s1, s2, s3)

