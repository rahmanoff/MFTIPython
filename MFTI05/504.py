""" Циклический сдвиг в массиве - влево. Через временную переменную, в которую помещается элемент с индексом 0.
Индекс идет слева - направо.
"""
N = 5
A = [0,1,2,3,4]
tmp = A[0]
print(A)
print(tmp)
for k in range(N-1):
    A[k] = A[k+1]
A[N-1] = tmp
print(A)