"""
"""
def two_sum(numbers, target):
   for i, k in enumerate(numbers):
       for j , l in enumerate(numbers):
           if k + l == target and i != j:
               return print(i, j)
        

def two_sum(nums, t):
    for i, x in enumerate(nums):
        for j, y in enumerate(nums):
            if i != j and x + y == t:
                return [i, j]    
a = [1,2,3,4,5,6]

b = 4

two_sum(a,b)