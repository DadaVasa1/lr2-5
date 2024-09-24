import math
a = float(input("Чему равно первое основание? "))
b = float(input("Чему равно второе основание? "))
c = float(input("Чему равна боковая сторона 1? "))
d = float(input("Чему равна боковая сторона 2? "))
p = (a + b + c + d) / 2
s = (a + b) / abs(a-b) * math.sqrt((p - a) * (p - b) * (p - a - c) * (p - a - d))


print ("Площадь трапеции равна: " , s)
