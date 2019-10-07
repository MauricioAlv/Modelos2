-- Mauricio Alvarado 

-- Función Fibonacci
fibo :: Int -> Int
fibo 0 = 0
fibo 1 = 1
fibo n = fibo (n-1) + fibo (n-2)

-- Potencia
potencia :: Int -> Int -> Int
potencia x n | (n==1) = x
             | even n = (potencia x (div n 2))* (potencia x (div n 2))
             | odd n = x * (potencia x (n-1))