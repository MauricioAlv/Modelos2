def validar(n):
  if (n>100):
    return True;
  return False;
  
n = int (input("ingrese un número: "))
if validar(n)==True:
  print ("Mayor a 100.")
else:
  print ("Menor a 100.")
