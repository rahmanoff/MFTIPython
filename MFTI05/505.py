# Решето Эратосфена
# Размер массива
N = 100
# Создание массива
A = [True] * N
# Задание 0 и 1 элементу значение False
A[0] = A[1] = False
# Если A[k] = True, 
for k in range (2,N):
    if A[k]:
        for m in range (2*k,N,k):
            A[m] = False
# print(A)
for k in range (N):
    print(k,'-', "простое" if A[k] else "составное")

