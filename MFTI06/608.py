# Сдать решение задачи D-Поиск максильного четного числа в последовательности
# 
# Последовательность состоит из натуральных чисел и завершается числом 0. 
# Определите значение наибольшего четного элемента последовательности. Числа, следующие за нулем, считывать не нужно.
#
# Формат входных данных
# Последовательность целых чисел, оканчивающаяся числом 0 (само число 0 в последовательность не входит). 
# Каждое число на новой строке.
# 
# Формат выходных данных
# Одно число — максимальное четное число в последовательности, если четные числа в ней присутствуют, иначе - 0.

A = [0]*999
Max = 0
x = int(input())
top = 0
i = 0
while x != 0:
    A[i] = int(x)
    i+=1
    top +=1
    x = int(input())
B = [0]*top
for i in range(top):
    B[i] = A[i]
    i+=1
for i in range (len(B)):
    if A[i]%2 == 0 and A[i]>Max:
        Max = A[i]
print(Max)