from math import sqrt

def pohyb_krala(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")

  vzdialenost = sqrt((x1 - x2)**2 + (y1 - y2)**2)
  if vzdialenost <= sqrt(2):
    return True
  return False


print(pohyb_krala(8, 1, 1, 1))  # False
print(pohyb_krala(4, 4, 5, 4))  # True