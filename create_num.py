"""
Преобдазование номера телефона.
"""

def create_phone_number(n):
    n.insert(0,'(')
    n.insert(4,')')
    n.insert(5,' ')
    n.insert(9,'-')
    return print("".join(map(str,n)))

create_phone_number([1,2,3,4,5,6,7,8,9,0])
'''
def create_phone_number1(n):
    n = "".join([str(x) for x in n] )
    return print("(" + str(n[0:3]) + ")" + " " + str(n[3:6]) + "-" + str(n[6:]))
create_phone_number1([1,2,3,4,5,6,7,8,9,0])
'''