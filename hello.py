

m = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
]

diag = [m[i][i] for i in [0, 1, 2]]
print(diag)
print(m)

doubles = [c * 2 for c in 'spam']
print(doubles)

G = (sum(row) for row in m)
print(next(G), next(G), next(G))
a = {1,'f',2,3,'ghb','хуй'}
print(a)

# 38:34. Видео английский. 