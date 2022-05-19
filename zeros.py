'''
'''
def zeros(n):
    count=0
    if n != 0:
        f = 1
        for i in range(2, n+1):
            f *= i
            k = str(f)
        
        
        for j in k[::-1]:
            if j == '0':
                count+=1
            else:
                break
    return print(count)

zeros(0)