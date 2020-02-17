#con recursividad
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
n=int(input("Ingrese el numero de factorial : "))
print(factorial(n))

#Con ciclos
factorial = 1
if int(n) >= 1:
  for i in range (1,int(n)+1):
    factorial = factorial * i
print("Factorial de ",n , " es: ",factorial)
