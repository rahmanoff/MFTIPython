# Сдать решение задачи F-Наибольший общий делитель
# 
# Необходимо найти НОД двух чисел, используя алгоритм Евклида.
#
# Формат входных данных
# На вход подаются два натуральных числа, по числу в новой строке.
#
# Формат выходных данных
# Одно число - НОД входных чисел.
Digit1 = int(input())
Digit2 = int(input())
while Digit1 != Digit2:
    if Digit1 > Digit2:
        Digit1 = Digit1 - Digit2
    else:
        Digit2 = Digit2 - Digit1
print(Digit1)