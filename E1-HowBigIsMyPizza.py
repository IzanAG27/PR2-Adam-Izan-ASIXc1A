"""
Grup: Izan Arnaiz, Adam Benahmed y Axel Benitez
Data Entrega: 16/10/2023
ASIX A1 M03 UF1
"""

import math

diametro = int(input("Dime el diametro en centimetros: "))

radio = diametro / 2  # El Radio lo obtenemos diviendo entre dos el diametro
superficie = math.pi * (radio ** 2)  # Calcula la superficie multiplicando PI por radio elevado al cuadrado
superficie = round(superficie, 2)  # Redondea la superficie a dos decimales

print(superficie)
