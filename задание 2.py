import math
x = float(input("Введите значение x: "))
y = float(input("Введите значение y: "))
z = float(input("Введите значение z: "))

s = abs(math.cos(x) - math.cos(y)) ** (1 + 2 * math.sin(y)**2) * (1 + z + z**2/2 + z**3/3 + z**4/4)

print("s = {0:.5f}".format(s))
