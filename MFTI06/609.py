# Сдать решение задачи E-Первое число трибоначчи, превосходящее заданное
# 
# Числа трибоначчи - последовательность целых чисел {t n }, заданная с помощью рекуррентного соотношения: 
# t(0) = 0, t(1) = 0, t(2) = 1 , t(n+3) = t(n) + t(n+1) + t(n+2) 
# Нужно найти номер первого числа трибоначчи, превосходящего заданное. Нумерация начинается с 0 .
#
# Формат входных данных
# Одно целое число.
#
# Формат выходных данных
# Одно число — номер первого числа трибоначчи, превосходящее заданное во входных данных число.
A = [0]*99
A[0] = A[1] = 0
A[2] = 1
for i in range(3,len(A)):
    A[i] = A[i-1]+A[i-2]+A[i-3]
Digit = int(input())
NextDigit = Digit
for i in range (len(A)):
    if A[i]>Digit:
        print(i)
        break