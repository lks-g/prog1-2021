from task14 import *
from task17 import *

def pohyb_damy(x1, y1, x2, y2):
  if (((x1 < 1) or (x1 > 8)) or ((y1 < 1) or ( y1 > 8)) or 
      ((x2 < 1) or (x2 > 8)) or ((y2 < 1) or ( y2 > 8))):
    raise ValueError("parametre musia nadobudat hodnotu z monoziny <1, 8>")
  
  if pohyb_veze(x1, y1, x2, y2) or pohyb_strelca(x1, y1, x2, y2):
    return True
  return False

print(pohyb_damy(1, 1, 2, 2))  # True
print(pohyb_damy(1, 1, 2, 3))  # False