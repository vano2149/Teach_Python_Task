"""
Страница 656! 
"""

def forLoop():
    res = []
    for x in repslist:
        res.appemd(x + 10)
    return res

def listComp():
    return [x + 10 for x in repslist]

def mapCall():
    return list(map((lambda x: x + 10), repslist))

def genExpr():
    return list(map((lambda x: x + 10), repslist))

def genExpr():
    return list(x + 10 for x in repslist)

def genFunc():
    def gen():
        for x in resplist:
            yield x + 10
    
    return list(gen())
