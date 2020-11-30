# Задача A-Грузовик

# Вы - водитель грузовика с открытым кузовом. 
# В кузове два груза: пианино и холодильник. 
# Пианино необходимо доставить в институт, холодильник в общежитие. 
# В каждое из этих мест ведет отдельная дорога, начинающаяся от перекрестка, на котором Вы стоите, других дорог в мире нет. 
# Известно, что по дороге в институт есть мост, 
# на котором действует ограничение максимальной допустимой массы автомобиля с грузом, 
# а по дороге в общежитие есть туннель с ограничением высоты. 
# Требуется определить, возможно ли доставить грузы или нет (разумеется, сгружать их, где попало, Вам запрещено).

# Формат входных данных
# На вход подается 8 чисел натуральных чисел (каждое < 100), каждое в новой строке, в следующем порядке: вес грузовика без груза, 
# высота платформы кузова (на которой стоят грузы), вес пианино, высота пианино, вес холодильника, высота холодильника, 
# максимальный допустимый вес на мосту, максимальная допустимая высота в туннеле

# Примечание: пианино и холодильник заведомо возвышаются над кабиной грузовика, т.е. высоту кабины можно в расчет не принимать.

# Формат выходных данных
# Вывести YES если доставка возможна и NO в противном случае.

TruckWeight = int(input())
TruckHeight = int(input())
PianoWeight = int(input())
PianoHeight = int(input())
RefWeight = int(input())
RefHeight = int(input())
MaxBridgeWeight = int(input())
MaxTunelHeight = int(input())

if PianoHeight >= RefHeight:
    MaxHeight = TruckHeight + PianoHeight
else:
    MaxHeight = TruckHeight + RefHeight

if ((TruckWeight + PianoWeight + RefWeight) <= MaxBridgeWeight) and ((TruckHeight + RefHeight) <= MaxTunelHeight):
    Route1 = True
else:
    Route1 = False

if (MaxHeight <= MaxTunelHeight) and ((TruckWeight + PianoWeight) <= MaxBridgeWeight):
    Route2 = True
else:
    Route2 = False

if Route1 or Route2:
    print('YES')
else:
    print('NO')