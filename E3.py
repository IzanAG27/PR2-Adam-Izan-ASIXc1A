numero1 = int(input("Dime un numero: "))
numero2 = int(input("Dime un numero: "))
numero3 = int(input("Dime un numero: "))
numero4 = int(input("Dime un numero: "))
numero5 = int(input("Dime un numero: "))
rango1 = range(numero1, numero2)
rango2 = range(numero3, numero4)
if numero5 in rango1 and numero5 in rango2:
    print(True)
else:
    print(False)