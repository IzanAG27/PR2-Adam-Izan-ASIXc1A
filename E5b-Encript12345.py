word = input("Que palabra quieres codificar? ")
word2 = "La palabra escogida es {}.".format(word)
print(word2)

if word != "":
    i = 0
    result = ""
    length = len(word)
    while i < length:
        if word[i] == 'a' or word[i] == 'A':
            result += '1'
            i += 1
        elif word[i] == 'e' or word[i] == 'E':
            result += '2'
            i += 1
        elif word[i] == 'i' or word[i] == 'I':
            result += '3'
            i += 1
        elif word[i] == 'o' or word[i] == 'O':
            result += '4'
            i += 1
        elif word[i] == 'u' or word[i] == 'U':
            result += '5'
            i += 1
        else:
            result += chr(ord(word[i]))
            i += 1
    print("La palabra codificada es {}.".format(result))
else:
    print("Introduce una palabra!")