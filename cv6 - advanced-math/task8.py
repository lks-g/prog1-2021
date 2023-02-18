from math import sqrt, log

cache = {}

def fibonacci(n):
  if n in cache:
    return cache[n]
  if n == 0:
    value = 0
  elif n == 1:
    value = 1
  else:
    value = fibonacci(n - 1) + fibonacci(n - 2)
  cache[n] = value
  return value

# Brute Force Method
def fibonacci_index(x):
  index = 0
  while True:
    fib_cislo = fibonacci(index)
    if fib_cislo == x:
      return index
    elif fib_cislo < x:
      index += 1
    else:
      return -1

# Mathematical Method
def fibonacci_index(x):
  a = 5 * x**2 + 4
  b = 5 * x**2 - 4
  a_sr = int(sqrt(a))
  b_sr = int(sqrt(b))
  if (a_sr * a_sr == a) or (b_sr * b_sr == b):
    fib_index = 2.078087 * log(x) + 1.672276
    return round(fib_index)
  else:
    return -1

print(fibonacci_index(4))  # -1
print(fibonacci_index(8))  # 6
print(fibonacci_index(2))  # 3
print(fibonacci_index(9))  # -1