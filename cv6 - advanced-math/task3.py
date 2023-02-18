def pow(base, exp):
  result = base
  counter = exp
  while counter > 1:
    result *= base
    counter -= 1
  return result

def najvacsie_x(n):
  if n < 0:
    return None
  x = 0
  while pow(2, x) < n and pow(2, x + 1) < n:
    x += 1
  return x

print(najvacsie_x(10))