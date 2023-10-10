import math

diametro = int(input("Dime el diametro en centimetros: "))
radio = diametro / 2
superficie = math.pi * (radio ** 2)
superficie = round(superficie, 2)

print(superficie)