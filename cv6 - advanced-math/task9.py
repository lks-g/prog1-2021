from math import sqrt
from random import uniform

def mysqrt(a):
  if a < 0:
    raise ValueError("Cannot square root negative number.")
  if a == 0:
    return 0.0
  if a == 1:
    return 1.0
  x = round(uniform(1, a-1), 4)
  tolerancia = 0.000001
  odchylka = tolerancia + 1
  while abs(odchylka) > tolerancia:
    x = (x + a / x) / 2
    odchylka = a - x**2
  return x

def test_square_root(do):
  print(" a   mysqrt(a) \t math.sqrt(a) \t diff")
  print(" -   --------- \t ------------\t----------------------")
  for a in range(1, do+1):
    my_fn = mysqrt(a)
    builtin_fn = sqrt(a)
    diff = round(my_fn, 11) - round(builtin_fn, 11)
    print("{: > 1}  {: >10}\t{: >10}\t{: >20}".format(a, round(my_fn, 8), round(builtin_fn, 8), diff))

test_square_root(9)