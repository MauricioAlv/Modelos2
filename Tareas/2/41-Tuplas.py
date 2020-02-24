
def contarCaracter(str): 

	vocales = 0
	consonantes = 0
	caracteres = 0
	digitos = 0

	for i in range(0, len(str)): 
		
		ch = str[i] 

		if ( (ch >= 'a' and ch <= 'z') or
			(ch >= 'A' and ch <= 'Z') ): 

			# Para el manejo de Mayúsculas
			ch = ch.lower() 

			if (ch == 'a' or ch == 'e' or ch == 'i'
						or ch == 'o' or ch == 'u'): 
				vocales += 1
			else: 
				consonantes += 1
		
		elif (ch >= '0' and ch <= '9'): 
			digitos += 1
		else: 
			caracteres += 1
	
	print("Vocales:", vocales) 
	print("Consonantes:", consonantes) 
	print("Digitos:", digitos) 
	print("Caracteres Especiales:", caracteres) 

# uso
str = input ("ingresa una palabra: ")

contarCaracter(str)
