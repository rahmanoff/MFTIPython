max = 0
num_max = 0
x = -1
while x != 0:
    x = int(input())
    if x > max:
        max =x 
        num_max = 1
    elif x == max:
        num_max += 1       
print(num_max)