"""
Grup: Izan Arnaiz, Adam Benahmed y Axel Benitez
Data Entrega: 16/10/2023
ASIX A1 M03 UF1
"""

word = input("Dime una palabra para codificar: ")

# Remplaza las vocales de una palabra por numeros del 1 al 5 independientemente si son mayusculas o minusculas
word = word.replace('a', '1')
word = word.replace('e', '2')
word = word.replace('i', '3')
word = word.replace('o', '4')
word = word.replace('u', '5')
word = word.replace('A', '1')
word = word.replace('E', '2')
word = word.replace('I', '3')
word = word.replace('O', '4')
word = word.replace('U', '5')

print("La palabra codificada es {}.".format(word))
# format() indica que la variable word la inserte como string entre las {}
