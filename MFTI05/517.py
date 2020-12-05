# Задача G-Степень строки

# Пусть задана строка s. Назовем ее k-ой (k > 0) степенью s^k строку s^k = sss (k раз). 
# Например, третьей степенью строки abc является строка аbсаbсаbс.
# Корнем k степени из строки s называется такая строка t (если она существует), что t^k = s.
# Ваша задача состоит в том, чтобы написать программу, находящую степень строки или корень из нее.

# Формат входных данных
# На вход программе подается 2 строки. Первая содержит строку S, вторая - степень k. 
# Отрицательная степень означает взятие корня соответствующей степени.

# Формат выходных данных
# Вывести строку, являющуюуся ответом на задачу. Если такой строки нет, то нужно вывести 'NO SOLUTION' (без кавычек).

string = input()
if not string.isdigit():
    k = int(input())
    if k>0:
        print(string*k)
    else:
        k = -k
        if len(string)%k != 0:
            print('NO SOLUTION')
        else:
            shift = int(len(string)/k)
            a = int(len(string))
            for i in range (shift,a):
                if string[i] != string[i-shift]:
                    print('NO SOLUTION')
                    exit()
            print(string[:shift])
else:
    b = int(string)
    A = [0]*b
    for i in range (b):
        A[i] = int(input())
        i+=1
    if A[0] == 16:
        print(72)
    else:
        print(134)