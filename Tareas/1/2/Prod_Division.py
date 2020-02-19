# Producto
def producto (n,m):
    if(m == 0):
        return 0
    if(m == 1):
        return n
    if(m > 1):
        return n + producto(n, m-1)
#Division
def division(n,m):
    if(n<m):
        return 0
    return division(n-m,m)+1

n = int (input ("Digite el valor de n"))
m = int (input ("Digite el valor de m"))
print("Division:"+ division(n,m))
print ("Producto" + producto(n,m))
