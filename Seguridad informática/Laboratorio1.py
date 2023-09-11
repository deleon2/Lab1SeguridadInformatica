# Universidad Finis Terrae
# Seguridad Informática, Laboratorio N°1
# Integrantes: Felipe Vera - Marcelo Ibarra



# Definición de funciones cifrado/descifrado #

def rot15(mensaje):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    cifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                cifrado= cifrado + alfabeto[(j+15)%26]
    return(cifrado)

def rot7(mensaje):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    cifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                cifrado= cifrado + alfabeto[(j+7)%26]
    return(cifrado)

def desrot15(mensaje):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    descifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                descifrado= descifrado + alfabeto[(j-15)%26]
        if (mensaje[i] == ' '):
            descifrado= descifrado + ' '
    return(descifrado)

def desrot7(mensaje):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    descifrado= ''
    for i in range(len(mensaje)):
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                descifrado= descifrado + alfabeto[(j-7)%26]
        if (mensaje[i] == ' '):
            descifrado= descifrado + ' '
    return(descifrado)


def vigenere(mensaje, llave):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    cifrado=''
    for i in range(len(mensaje)):
        temp1=''
        temp2=''
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                temp1= j
            if (llave[i%len(llave)] == alfabeto[j]):
                temp2= j
        if (temp1 != '' and temp2 != ''):
            cifrado= cifrado+alfabeto[(temp1+temp2)%26]
    return(cifrado)

def desvigenere(mensaje, llave):
    alfabeto= 'abcdefghijklmnopqrstuvwxyz'
    descifrado=''
    for i in range(len(mensaje)):
        temp1=''
        temp2=''
        for j in range(len(alfabeto)):
            if (mensaje[i] == alfabeto[j]):
                temp1= j
            if (llave[i%len(llave)] == alfabeto[j]):
                temp2= j
            
        if (temp1 != '' and temp2 != ''):
            descifrado= descifrado+alfabeto[(temp1-temp2)%26]
        else:
            descifrado= descifrado+' '

    return(descifrado)

                


# Implementación de funciones para los desafíos 1 y 2 #

print(rot15(vigenere(rot7('holamundo'), 'cvqnoteshrwnszhhksorbqcoas')))

print(desrot7(desvigenere(desrot15('oemkd lyzqgvqxgptuuinqy nrkkfmnv'), 'aobkqolrzsrigpknkufezioer')))















    
                
