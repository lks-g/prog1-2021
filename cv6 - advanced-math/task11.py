from math import factorial, sqrt

def estimate_pi():
  const = 2 * sqrt(2) / 9801
  c = 0
  result = 0
  while True:
    numerator = factorial(4*c) * (1103 + 26390*c) 
    denominator = factorial(c)**4 * 396**(4*c) 
    res = numerator / denominator
    result += res
    if res < 10e-15:
      return 1 / (result * const)
    c += 1

print(estimate_pi())