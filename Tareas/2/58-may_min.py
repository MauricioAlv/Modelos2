# Convetir en opuesta
def convertirOpuesta(str):
    ln = len(str)

    # Conversion valores ASCII
    for i in range(ln):
        if str[i] >= 'a' and str[i] <= 'z':

            # Conversion
            str[i] = chr(ord(str[i]) - 32)

        elif str[i] >= 'A' and str[i] <= 'Z':

            # Conversion
            str[i] = chr(ord(str[i]) + 32)

def main():
    # Valor recibido
    string = input("Ingrese un texto: ")
    #Convertir lista
    string = list(string)

    #llamdo
    convertirOpuesta(string)

    #Volver String
    string = ''.join(string)
    print(string)

main()
