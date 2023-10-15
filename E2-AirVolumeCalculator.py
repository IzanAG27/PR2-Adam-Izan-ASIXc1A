"""
Grup: Izan Arnaiz, Adam Benahmed y Axel Benitez
Data Entrega: 16/10/2023
ASIX A1 M03 UF1
"""

ancho = int(input("Dime el ancho: "))
altura = int(input("Dime la altura: "))
largo = int(input("Dime el largo: "))

# Para obtener el volumen de aire dentro de una habitacion deberemos multiplicar el ancho por la altura por el largo
aire = ancho * altura * largo

print("El volum de l'aula es {} m³".format(aire))
# format() indica que la variable aire la inserte como string entre las {}
