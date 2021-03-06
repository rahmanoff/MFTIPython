# Сдать решение задачи I-Максимум неполного массива

# В некотором физическом эксперименте показания прибора снимались с частотой 5 измерений в секунду. 
# Эксперимент проводился в течение довольно большого времени, и в результате накопилось очень много данных. 
# Ученых, которые проводили данный эксперимент, очень интересует, 
# какое максимальное значение измеряемой величины достигалось во время измерения. 
# Но вот беда: на остановку установки также требуется секунда времени, 
# и в течение этого времени с установки могут приходить совершенно любые значения величины. 
# В связи с этим, показания последних 5 измерений учитывать при поиске максимального значения не следует.

# Вам необходимо написать программу, которая в данном потоке чисел заранее неизвестной длины находит максимальное значение, 
# отбрасывая при этом последние 5 измерений.

# Формат входных данных
# На вход вашей программе передается последовательность натуральных чисел -- результаты измерений. 
# Каждое новое число передается с новой строки. 
# Гарантируется, что длина входной последовательности не меньше 6 и не превосходит 10 в степени 9. 
# На конце последовательности передается число 0.

# Формат выходных данных
# Программа должна вывести на экран одно число -- максимальное значение входной последовательности 
# за исключением последних 5 элементов.

A = [0]*9 # Создаем массив для хранения данных, длиной 9 элементов
B = [0]*5 # Создаем массив для отсекания лишних данных
total_max = 0 # Задаем начальное значение максимума
while True:
    x = int(input()) # Ввод данных
    if x == 0: # Мониторим окончание ввода данных
        break
    A.append(x) # Добавляем данные в массив
    B = A[:5] # Формируем массив для валидных данных
    if total_max < max(B): # Сравниваем глобальный максимум с локальным максимумом в выборке
        total_max = max(B) # Если глобальный максимум меньше локального, то значение локального максимума передем в глобальный
    if len(A) > 9: # Мониторим размер окна выборки, если больше 9, то уменьшаеем на 1
        A.pop(0)
print(total_max) # Выводим значение максимума
