import math

def problem_1(Nmax):
  M3 = []
  M5 = []
  for i in range(Nmax):
    if (i * 3):
      M3.append(i)
    if(i * 5):
      M5.append(i)
      
  L1 = set(M3)
  L2 = set(M5)
  resultado = list(L1.union(L2))
  M = sum(resultado)
  
  return(M)

def problem_2(Nmax):
  a, b = 1, 2
  suma = 0

  while a <= Nmax:
    suma += a
    a, b = b, a + b
    
  return suma

def problem_3(Nmax):
  factores_primos = []
  factor = 2
  while factor * factor <= Nmax:
    if Nmax % factor == 0:
      factores_primos.append(factor)
      Nmax //= factor
    else:
      factor += 1
    if Nmax > 1:
      factores_primos.append(Nmax)

  return factores_primos

def problem_4():
  palindromo_max = 0
  for i in range(100, 1000):
    for j in range(100, 1000):
      producto = i * j
      if producto <= 999 and str(producto) == str(producto)[::-1] and producto > palindromo_max:
        palindromo_max = producto
  return palindromo_max

def problem_5(fin):
  inicio = 1
  resultado = 1
  for i in range(inicio, fin + 1):
    resultado = math.lcm(resultado, i)
  return resultado