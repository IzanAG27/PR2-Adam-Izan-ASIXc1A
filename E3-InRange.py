"""
Grup: Izan Arnaiz, Adam Benahmed y Axel Benitez
Data Entrega: 16/10/2023
ASIX A1 M03 UF1
"""

numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime un numero: "))
numero3 = int(input("Dime un numero: "))
numero4 = int(input("Dime un numero: "))
numero5 = int(input("Dime un numero: "))

rango1 = range(numero1, numero2)  # Define dos rangos de numeros dado el valor de las variables
rango2 = range(numero3, numero4)

if numero5 in rango1 and numero5 in rango2:  # Coge la variable numero5  e indica si el valor esta dentro de los dos rangos
    print(True)
else:
    print(False)
